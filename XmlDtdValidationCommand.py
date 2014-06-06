import sublime, sublime_plugin

class XmlDtdValidationCommand(sublime_plugin.WindowCommand):
    def run(self):
    	context = self.window
    	context.run_command('set_build_system', {"file": "Packages/scribenet-sublime-validation/XML DTD Validation.sublime-build"})
    	context.run_command('build');