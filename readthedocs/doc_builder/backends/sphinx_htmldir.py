import logging
import os
import shutil

from doc_builder.base import restoring_chdir
from doc_builder.backends.sphinx import Builder as HtmlBuilder
from projects.utils import run
from core.utils import copy_to_app_servers, copy_to_dotcloud_static
from django.conf import settings

log = logging.getLogger(__name__)


class Builder(HtmlBuilder):

    @restoring_chdir
    def build(self, **kwargs):
        project = self.version.project

        log.info("removing the files from the original build directory")
        try:
            shutil.rmtree(project.full_build_path(self.version.slug))
        except:
            log.info("files do not exist, continue")

        os.chdir(self.version.project.conf_dir(self.version.slug))
        if project.use_virtualenv:
            build_command = '%s -b dirhtml . _build/html' % project.venv_bin(
                version=self.version.slug, bin='sphinx-build')
        else:
            build_command = "sphinx-build -b dirhtml . _build/html"
        build_results = run(build_command)
        if 'no targets are out of date.' in build_results[1]:
            self._changed = False
        return build_results

    def move(self, **kwargs):
        project = self.version.project
        if project.full_build_path(self.version.slug):
            target = project.rtd_build_path(self.version.slug)
            if "_" in project.slug:
                new_slug = project.slug.replace('_', '-')
                new_target = target.replace(project.slug, new_slug)
                #Only replace 1, so user_builds doesn't get replaced >:x
                targets = [target, new_target]
            else:
                targets = [target]
            for target in targets:
                if getattr(settings, "MULTIPLE_APP_SERVERS", None):
                    log.info("Copying docs to remote server.")

                    #copy_to_app_servers(
                    #    project.full_build_path(self.version.slug), target)

                    #also copy it using rsync to the static app.
                    # copy_to_dotcloud_static(project.full_build_path(self.version.slug), target)
                else:
                    outdir = "{0}/{1}/".format(project.slug, self.version.slug)
                    log.info("Copying docs to remote server.")
                    copy_to_dotcloud_static(project.full_build_path(self.version.slug), outdir)
                    if os.path.exists(target):
                        shutil.rmtree(target)
                    log.info("Copying docs on the local filesystem")
                    shutil.copytree(project.full_build_path(self.version.slug),
                                    target)
        else:
            log.warning("Not moving docs, because the build dir is unknown.")

