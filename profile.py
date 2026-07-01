# Generated using https://godot-build-options-generator.github.io

from os import environ

# extra_suffix = ""

isRelease = environ.get("DEBUG") is None

target = "template_release" if isRelease else "template_debug"
production = "yes" if isRelease else "no"

# clangd support
compiledb = "yes"

deprecated = "no"
minizip = "no"

# disable 3d
disable_3d = "yes"
disable_physics_3d = "yes"
module_meshoptimizer_enabled = "no"

# disable networking
module_enet_enabled = "no"
module_jsonrpc_enabled = "no"
module_mbedtls_enabled = "no"
module_multiplayer_enabled = "no"
module_upnp_enabled = "no"
module_webrtc_enabled = "no"
module_websocket_enabled = "no"
module_webxr_enabled = "no"

# disable vr
module_mobile_vr_enabled = "no"
module_openxr_enabled = "no"

# disable webcam support
module_camera_enabled = "no"

# simple text
module_text_server_adv_enabled = "no"
module_text_server_fb_enabled = "yes"

lto = "full" if isRelease else "none"

# image formats
module_bmp_enabled = "no"
module_dds_enabled = "no"
module_jpg_enabled = "no"
module_ktx_enabled = "no"
module_svg_enabled = "no"
module_tga_enabled = "no"
module_tinyexr_enabled = "no"
# module_webp_enabled = "no"

# other
module_raycast_enabled = "no"
