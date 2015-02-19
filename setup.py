#!/usr/bin/python

# python setup.py sdist --format=zip,gztar

from setuptools import setup
import os
import sys
import platform
import imp


version = imp.load_source('version', 'lib/version.py')
util = imp.load_source('util', 'lib/util.py')

if sys.version_info[:3] < (2, 7, 0):
    sys.exit("Error: Electrum-nmc requires Python version >= 2.7.0...")



if (len(sys.argv) > 1) and (sys.argv[1] == "install"): 
    # or (platform.system() != 'Windows' and platform.system() != 'Darwin'):
    print "Including all files"
    data_files = []
    usr_share = util.usr_share_dir()
    if not os.access(usr_share, os.W_OK):
        try:
            os.mkdir(usr_share)
        except:
            sys.exit("Error: cannot write to %s.\nIf you do not have root permissions, you may install Electrum-nmc in a virtualenv.\nAlso, please note that you can run Electrum-nmc without installing it on your system."%usr_share)

    data_files += [
        (os.path.join(usr_share, 'applications/'), ['electrum-nmc.desktop']),
        (os.path.join(usr_share, 'app-install', 'icons/'), ['icons/electrum-nmc.png'])
    ]
    if not os.path.exists('locale'):
        os.mkdir('locale')
    for lang in os.listdir('locale'):
        if os.path.exists('locale/%s/LC_MESSAGES/electrum.mo' % lang):
            data_files.append((os.path.join(usr_share, 'locale/%s/LC_MESSAGES' % lang), ['locale/%s/LC_MESSAGES/electrum.mo' % lang]))


    appdata_dir = os.path.join(usr_share, "electrum-nmc")
    data_files += [
        (appdata_dir, ["data/README"]),
        (os.path.join(appdata_dir, "cleanlook"), [
            "data/cleanlook/name.cfg",
            "data/cleanlook/style.css"
        ]),
        (os.path.join(appdata_dir, "sahara"), [
            "data/sahara/name.cfg",
            "data/sahara/style.css"
        ]),
        (os.path.join(appdata_dir, "dark"), [
            "data/dark/name.cfg",
            "data/dark/style.css"
        ])
    ]

    for lang in os.listdir('data/wordlist'):
        data_files.append((os.path.join(appdata_dir, 'wordlist'), ['data/wordlist/%s' % lang]))
else:
    data_files = []

setup(
    name="Electrum-nmc",
    version=version.ELECTRUM_VERSION,
    install_requires=[
        'slowaes>=0.1a1',
        'ecdsa>=0.9',
        'pbkdf2',
        'requests',
        'pyasn1',
        'pyasn1-modules',
        'qrcode',
        'SocksiPy-branch',
        'protobuf',
        'tlslite'
    ],
    package_dir={
        'electrum_nmc': 'lib',
        'electrum_nmc_gui': 'gui',
        'electrum_nmc_plugins': 'plugins',
    },
    scripts=['electrum'],
    data_files=data_files,
    py_modules=[
        'electrum_nmc.account',
        'electrum_nmc.bitcoin',
        'electrum_nmc.blockchain',
        'electrum_nmc.bmp',
        'electrum_nmc.commands',
        'electrum_nmc.daemon',
        'electrum_nmc.i18n',
        'electrum_nmc.interface',
        'electrum_nmc.mnemonic',
        'electrum_nmc.msqr',
        'electrum_nmc.network',
        'electrum_nmc.network_proxy',
        'electrum_nmc.old_mnemonic',
        'electrum_nmc.paymentrequest',
        'electrum_nmc.paymentrequest_pb2',
        'electrum_nmc.plugins',
        'electrum_nmc.qrscanner',
        'electrum_nmc.simple_config',
        'electrum_nmc.synchronizer',
        'electrum_nmc.transaction',
        'electrum_nmc.util',
        'electrum_nmc.verifier',
        'electrum_nmc.version',
        'electrum_nmc.wallet',
        'electrum_nmc.x509',
        'electrum_nmc_gui.gtk',
        'electrum_nmc_gui.qt.__init__',
        'electrum_nmc_gui.qt.amountedit',
        'electrum_nmc_gui.qt.console',
        'electrum_nmc_gui.qt.history_widget',
        'electrum_nmc_gui.qt.icons_rc',
        'electrum_nmc_gui.qt.installwizard',
        'electrum_nmc_gui.qt.lite_window',
        'electrum_nmc_gui.qt.main_window',
        'electrum_nmc_gui.qt.network_dialog',
        'electrum_nmc_gui.qt.password_dialog',
        'electrum_nmc_gui.qt.paytoedit',
        'electrum_nmc_gui.qt.qrcodewidget',
        'electrum_nmc_gui.qt.qrtextedit',
        'electrum_nmc_gui.qt.qrwindow',
        'electrum_nmc_gui.qt.receiving_widget',
        'electrum_nmc_gui.qt.seed_dialog',
        'electrum_nmc_gui.qt.transaction_dialog',
        'electrum_nmc_gui.qt.util',
        'electrum_nmc_gui.qt.version_getter',
        'electrum_nmc_gui.stdio',
        'electrum_nmc_gui.text',
        'electrum_nmc_plugins.btchipwallet',
        'electrum_nmc_plugins.coinbase_buyback',
        'electrum_nmc_plugins.cosigner_pool',
        'electrum_nmc_plugins.exchange_rate',
        'electrum_nmc_plugins.greenaddress_instant',
        'electrum_nmc_plugins.labels',
        'electrum_nmc_plugins.trezor',
        'electrum_nmc_plugins.virtualkeyboard',
        'electrum_nmc_plugins.plot',

    ],
    description="Lightweight Namecoin Wallet",
    author="Thomas Voegtlin",
    author_email="thomasv1@gmx.de",
    license="GNU GPLv3",
    url="https://electrum.org",
    long_description="""Lightweight Namecoin Wallet"""
)
