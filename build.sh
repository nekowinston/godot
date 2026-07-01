#!/usr/bin/env bash

cd "$(dirname "$0")" || exit

if [[ -n "$container" ]]; then
	podman run --rm -it \
		-v "${PWD}:/src" \
		-e SCRIPT_AES256_ENCRYPTION_KEY \
		godot-builder
	"/src/build.sh"
else
	scons profile=./profile.py build_profile=./build.gdbuild

	export DEBUG=1
	scons profile=./profile.py build_profile=./build.gdbuild
	unset DEBUG
fi
