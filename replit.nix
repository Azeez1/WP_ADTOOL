{pkgs}: {
  deps = [
    pkgs.python311Packages.uvicorn
    pkgs.python312Packages.uvicorn
  ];
}
