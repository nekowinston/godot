{
  pkgs ? import <nixpkgs> {
    config = { };
    overlays = [ ];
  },
}:
pkgs.mkShell {
  inputsFrom = [
    pkgs.godotPackages_4_6.godot
  ];

  nativeBuildInputs = with pkgs; [
    clang-tools
  ];
}
