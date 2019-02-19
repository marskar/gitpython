from virtualenvapi.manage import VirtualEnvironment
env = VirtualEnvironment('.')
env.install('pandas')
print(env.installed_package_names)
print(env.installed_packages)
print(env.name)
print(env.root)
print(env.is_installed('pandas'))
