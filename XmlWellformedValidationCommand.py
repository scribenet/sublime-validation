import sublime, sublime_plugin

class XmlWellformedValidationCommand(sublime_plugin.WindowCommand):
    def run(self):
    	context = self.window
    	context.run_command('set_build_system', {"file": "Packages/scribenet-sublime-validation/XML Well-Formed Check.sublime-build"})
    	context.run_command('build');