import os, sys
from glob import glob

# Configuration
BUILD_DIR        = 'build'
PROJECT_DIR      = 'src'
PLATFORM_TOOLSET = 'v140'
F4SE_REVISION    = 'tags/v0.6.20'
BUILD_TOOLS_DIR  = 'tools/build-tools'

num_build_success = 0
paths = glob('mods/*/')
for path in paths:
    # Build plugin
    build_dir   = f'{path}/{BUILD_DIR}'
    project_dir = f'{path}/{PROJECT_DIR}'
    buildOK = os.system(f'python {path}/tools/build-tools/build_plugin.py "{build_dir}" "{project_dir}" "{PLATFORM_TOOLSET}" "{F4SE_REVISION}"')
    if buildOK != 0:
        print(f'WARNING: {path} failed to build.')
    else:
        # Package plugin
        if os.path.exists(f'{path}/dist'):
            PLUGIN_LOCATION_PATTERN = f'{build_dir}/x64/Release/*.dll'
            DIST_DIR = f'{path}/dist'
            packageOK = os.system(f'python {BUILD_TOOLS_DIR}/package_plugin.py "{PLUGIN_LOCATION_PATTERN}" "{DIST_DIR}" "{BUILD_DIR}" "{project_dir}"')
            if packageOK != 0:
                print(f'WARNING: {path} failed to package.')
            else:
                num_build_success += 1

print(f'FINISHED: Successfully built {num_build_success}/{len(paths)} packages.')