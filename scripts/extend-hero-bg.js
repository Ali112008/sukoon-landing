import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

async function main() {
  const zai = await ZAI.create();

  // Read the portrait image and convert to base64 data URL
  const imageBuffer = fs.readFileSync('/home/z/my-project/assets/images/hero-bg-new.png');
  const base64Image = imageBuffer.toString('base64');
  const dataUrl = `data:image/png;base64,${base64Image}`;

  console.log('📸 Sending image edit request...');

  const response = await zai.images.generations.edit({
    prompt: 'Extend this bedroom photo to a wide landscape format. Keep the man sleeping on the white pillow on the right side of the frame. Extend the room to the left showing more of the bedroom with a dark navy blue wall, a bedside table with a decorative lamp, soft ambient evening lighting. Maintain the calm, serene, luxurious mood. The image should work as a hero section background for a premium pillow brand. Keep the upper area with dark gradient for white text overlay. Professional product photography quality.',
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
