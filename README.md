# nixtrobed
nixtrobed is a tiny wrapper around Vagrant and Ansible to easily create a number of VMs. Its main use case is to test software and scripts etc. on different distributions.

## Usage
```
Usage: nixtrobed [OPTIONS] COMMAND [ARGS]...

Options:
  -h, --help  Show this message and exit.

Commands:
  init       Generate and initialize a new testbed directory.
  provision  Provision the boxes of the given distributions.
  start      Start the boxes of the given distributions.
  stop       Stop the boxes of the given distributions.
```

### Initializing a new nixtrobed directory
The first step is to create a new folder. The command to use is `nixtrobed init`:
```
Usage: nixtrobed init DIRECTORY

  Generate and initialize a new testbed directory.

  DIRECTORY is the target directory. This must not exist yet.
```
For example:
```
$ nixtrobed init some-folder
$ tree -r some-folder 
some-folder
├── Vagrantfile.jinja
├── provisioning
│   ├── roles
│   └── playbooks
│       └── default.yml
└── nixtrobed.distros
```
