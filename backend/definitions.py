from os.path import dirname, abspath, join

# Root backend directory
# join used here to eliminate problems with different filesystem formats
ROOT_DIR = dirname(abspath(__file__))
SRC_DIR = join(ROOT_DIR, "src/")
CONF_PATH = join(ROOT_DIR, "conf/")
