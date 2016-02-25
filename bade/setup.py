from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')

setup(
    name = "Bad Encounter",
    description = "Jeu créé à l'occasion des TPEs de 2016 par Eyal CHOJNOWSKI, Alycia MOLLE et Maréva SEI",
    options = {'py2exe': {'bundle_files': 0,
                          'compressed': True,
                          'optimize': 1,
                          'dist_dir': 'build\\'
                          }
               },
    windows = ['program.py'],
    zipfile = None,
)
