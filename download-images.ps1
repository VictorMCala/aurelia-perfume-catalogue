# =============================================================================
#  AURÉLIA — Real bottle photo downloader (for DEMO use)
# =============================================================================
#  The catalogue shows original, distinct drawn flacons by default. To swap in
#  REAL product photos for a demo, paste a direct image URL for each fragrance
#  below (right-click an image in your browser → "Copy image address"), then run:
#
#      powershell -ExecutionPolicy Bypass -File .\download-images.ps1
#
#  Files are saved into .\images with the exact names the catalogue expects.
#  Prefer PNGs with transparent backgrounds for the cleanest result; JPGs work
#  too (rename the target to .jpg and update the <img src> in catalogue.html).
#
#  NOTE: Product photos are the property of their respective brands/retailers.
#  Use only for a private demo/mock-up, not for publication or resale.
# =============================================================================

$ErrorActionPreference = 'Stop'
$ProgressPreference    = 'SilentlyContinue'
$dir = Join-Path $PSScriptRoot 'images'
New-Item -ItemType Directory -Force -Path $dir | Out-Null

# ---- Paste a direct image URL between the quotes for each item you want ----
#      (open the reference page in the comment, right-click the bottle
#       image -> "Copy image address", paste it here)
$images = [ordered]@{
  '01-baccarat-rouge-540' = ''   # ref: https://www.notino.com/maison-francis-kurkdjian/baccarat-rouge-540-eau-de-parfum-unisex/
  '02-coco-mademoiselle'  = ''   # ref: https://www.notino.com/chanel/coco-mademoiselle-eau-de-parfum-for-women/
  '03-delina'             = ''   # ref: https://www.notino.com/parfums-de-marly/delina-eau-de-parfum-for-women/
  '04-libre'              = ''   # ref: https://www.notino.com/yves-saint-laurent/libre-eau-de-parfum-for-women/
  '05-black-opium'        = ''   # ref: https://www.notino.com/yves-saint-laurent/black-opium-eau-de-parfum-for-women/
  '06-good-girl'          = ''   # ref: https://www.notino.com/carolina-herrera/good-girl-eau-de-parfum-for-women/
  '07-jadore'             = ''   # ref: https://www.notino.com/dior/jadore-eau-de-parfum-for-women/
  '08-si'                 = ''   # ref: https://www.notino.com/giorgio-armani/si-eau-de-parfum-for-women/
  '09-paradoxe'           = ''   # ref: https://www.notino.com/prada/paradoxe-eau-de-parfum-for-women/
  '10-aventus'            = ''   # ref: https://www.notino.com/creed/aventus-eau-de-parfum-for-men/
  '11-sauvage'            = ''   # ref: https://www.notino.com/dior/sauvage-eau-de-parfum-for-men/
  '12-bleu-de-chanel'     = ''   # ref: https://www.notino.com/chanel/bleu-de-chanel-eau-de-parfum-for-men/
  '13-naxos'              = ''   # ref: https://www.notino.com/xerjoff/naxos-eau-de-parfum-unisex/
  '14-myslf'              = ''   # ref: https://www.notino.com/yves-saint-laurent/myslf-eau-de-parfum-for-men/
  '15-layton'             = ''   # ref: https://www.notino.com/parfums-de-marly/layton-eau-de-parfum-unisex/
  '16-oud-wood'           = ''   # ref: https://www.notino.com/tom-ford/oud-wood-eau-de-parfum-unisex/
  '17-tobacco-vanille'    = ''   # ref: https://www.notino.com/tom-ford/tobacco-vanille-eau-de-parfum-unisex/
  '18-erba-pura'          = ''   # ref: https://www.notino.com/sospiro/erba-pura-eau-de-parfum-unisex/
  '19-born-in-roma'       = ''   # ref: https://www.notino.com/valentino/born-in-roma-eau-de-parfum-for-women/
  '20-angels-share'       = ''   # ref: https://www.notino.com/by-kilian/angels-share-eau-de-parfum-unisex/
}

$headers = @{ 'User-Agent' = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36' }
$done = 0; $skipped = 0

foreach ($name in $images.Keys) {
  $url = $images[$name]
  if ([string]::IsNullOrWhiteSpace($url)) { Write-Host "skip  $name (no URL)" -ForegroundColor DarkGray; $skipped++; continue }
  $ext = ([System.IO.Path]::GetExtension(($url -split '\?')[0]))
  if ($ext -notmatch '^\.(png|jpg|jpeg|webp)$') { $ext = '.png' }
  $out = Join-Path $dir "$name$ext"
  try {
    Invoke-WebRequest -Uri $url -Headers $headers -OutFile $out -UseBasicParsing -TimeoutSec 30
    Write-Host "ok    $name  ->  $([System.IO.Path]::GetFileName($out))" -ForegroundColor Green
    $done++
  } catch {
    Write-Host "FAIL  $name  ($($_.Exception.Message))" -ForegroundColor Red
  }
}

Write-Host ""
Write-Host "Downloaded $done, skipped $skipped. Any missing photo falls back to the drawn flacon automatically." -ForegroundColor Cyan
Write-Host "If you saved a .jpg/.webp, update that fragrance's <img src> extension in catalogue.html." -ForegroundColor Cyan
