param([int]$Port = 8000)

$ErrorActionPreference = "SilentlyContinue"
$pids = (Get-NetTCPConnection -LocalPort $Port -ErrorAction SilentlyContinue).OwningProcess | Select-Object -Unique
if ($pids) {
  $pids | ForEach-Object { Stop-Process -Id $_ -Force -ErrorAction SilentlyContinue }
  "Stopped: $($pids -join ', ') on port $Port."
} else {
  "Nothing listening on port $Port."
}
