param(
  [int]$Port = 8000,
  [string]$BindHost = "127.0.0.1"
)

$ErrorActionPreference = "SilentlyContinue"

# 1) venv aktivieren (falls vorhanden)
if (Test-Path ".\.venv\Scripts\Activate.ps1") {
  . .\.venv\Scripts\Activate.ps1
}

# 2) Port freiräumen
$pids = (Get-NetTCPConnection -LocalPort $Port -ErrorAction SilentlyContinue).OwningProcess | Select-Object -Unique
if ($pids) {
  $pids | ForEach-Object { Stop-Process -Id $_ -Force -ErrorAction SilentlyContinue }
  Write-Host "Freigegeben: Port $Port (gekilled: $($pids -join ', '))"
} else {
  Write-Host "Port $Port war frei."
}

# 3) Uvicorn stabil starten (nur app/ beobachten, problematische Ordner excluden)
uvicorn app.main:app `
  --host $BindHost `
  --port $Port `
  --reload `
  --reload-dir app `
  --reload-exclude ".venv/*" `
  --reload-exclude "uploads/*"
