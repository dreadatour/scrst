# Dropzone Action Info
# Name: ScrSt
# Description: Upload image as screenshot
# Handles: Files
# Creator: Vladimir Rudnyh
# URL: https://github.com/dreadatour/scrst
# Events: Dragged, Clicked
# KeyModifiers: No
# SkipConfig: No
# RunsSandboxed: No
# Version: 1.0
# MinDropzoneVersion: 3.0

def dragged
  $dz.determinate(true)
  $dz.percent(0)

  result = system('/usr/local/bin/scrst', $items[0])
  if result.nil?
    $dz.fail("Error uploading image #{$?}")
  end

  $dz.percent(100)
  $dz.url(false)
end

def clicked
  $dz.determinate(true)
  $dz.percent(0)

  result = system('/usr/local/bin/scrst')
  if result.nil?
      $dz.fail("Error uploading image #{$?}")
  end

  $dz.percent(100)
  $dz.url(false)
end
