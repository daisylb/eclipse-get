#!/usr/bin/env python2.7

#Note: This file is run standalone from the shell, and is renamed to eclipse-get in the isntall process.
#It's only called eclipse_get.py here so Eclipse plays nice.

from subprocess import call
import argparse
import yaml

RELEASE = 'indigo'

#p2 director docs: http://help.eclipse.org/indigo/index.jsp?topic=/org.eclipse.platform.doc.isv/guide/p2_director.html

#argument parser
parser = argparse.ArgumentParser(
	description='Provides a friendly interface to installing Eclipse packages on the command line.')
parser.add_argument(
	'action',
	choices=['install','list'],
	type=str,
	help='List available package names, or install a package')
parser.add_argument(
	'packages',
	metavar='package_name', 
	type=str,
	nargs='*',
	help='Package names. Required when installing.')
parser.add_argument(
	'--eclipse',
	dest='eclipse',
	type=str,
	nargs='?',
	help='Path to Eclipse binary. Defaults to /opt/eclipse/eclipse',
	default='/opt/eclipse/eclipse')
parser.add_argument(
	'--pkgfile',
	dest='pkgfile',
	type=str,
	nargs='?',
	help='Path to eclipse-get package file. Defaults to /opt/eclipse-get/data/packages.yaml',
	default='/opt/eclipse-get/data/packages.yaml')
parser.add_argument(
	'--dry-run',
	dest='dryrun',
	action='store_true',
	help='Doesn\'t perform the install, just prints commands.')
args = parser.parse_args()


#YAML parser
with open(args.pkgfile) as f:
	pkgfile = yaml.load(f.read())

if args.action == 'list':
	for k, v in pkgfile['packages'].iteritems():
		print k

elif args.action == 'install':
	for pkgname in args.packages:
		print "Installing %s..." % pkgname
	
		pkg = pkgfile['packages'][pkgname]
		iu = pkg['iu']
		repo = pkg.get('repo', pkgfile['default-repos'][RELEASE])
	
		cmd = [
			args.eclipse,
			'-nosplash',
			'-application', 'org.eclipse.equinox.p2.director',
			'-repository', repo,
			'-installIU', iu,
		]
		if args.dryrun:
			print " ".join(cmd)
		else:
			call(cmd)
		
