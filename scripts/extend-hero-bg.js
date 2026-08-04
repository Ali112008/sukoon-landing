import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

async function main() {
  const zai = await ZAI.create();

  // Read the ORIGINAL client photo
  const imageBuffer = fs.readFileSync('/home/z/my-project/assets/images/hero-bg-new.png');
  const base64Image = imageBuffer.toString('base64');
  const dataUrl = `data:image/png;base64,${base64Image}`;

  console.log('📸 Sending image edit request with ORIGINAL client photo...');

  const response = await zai.images.generations.edit({
    prompt: 'Widen this photo to a landscape format. The man sleeping on the white pillow MUST remain clearly visible on the right side of the frame. Extend the bedroom scene to the left side - show more of the bed, headboard, and bedside table with lamp. Keep the same warm lighting, same brown headboard, same blue shirt, same white pillow. This is a real photo - maintain photorealistic quality. Do NOT change the person or pillow at all.',
    images: [{ url: dataUrl }],
    size: '1440x720'
  });

  const imageBase64 = response.data[0].base64;
  const buffer = Buffer.from(imageBase64, 'base64');
  
  const outputPath = '/home/z/my-project/assets/images/hero-bg-desktop.png';
  fs.writeFileSync(outputPath, buffer);
  
  console.log(`✅ Desktop hero background saved: ${outputPath}`);
  console.log(`   Size: ${(buffer.length / 1024).toFixed(0)} KB`);
}

main().catch(err => {
  console.error('❌ Error:', err.message);
  process.exit(1);
});
