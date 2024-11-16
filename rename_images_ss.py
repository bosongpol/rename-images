import os
import re
import shutil

def rename_product_images():
    print("\n=== โปรแกรมเปลี่ยนชื่อรูปภาพสินค้า + สร้าง Screenshot ===\n")
    
    # ให้ผู้ใช้ป้อนพาธของโฟลเดอร์
    print("กรุณาลากโฟลเดอร์ที่มีรูปภาพมาวางที่นี่ แล้วกด Enter:")
    folder_path = input().strip('"')  # ลบเครื่องหมาย " ออก
    
    if not os.path.exists(folder_path):
        print("\nไม่พบโฟลเดอร์ที่ระบุ กรุณาตรวจสอบอีกครั้ง")
        input("กด Enter เพื่อปิดโปรแกรม...")
        return
    
    # รวบรวมไฟล์ทั้งหมดในโฟลเดอร์
    files = os.listdir(folder_path)
    
    # กรองเฉพาะไฟล์รูปภาพ
    image_files = [f for f in files if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    
    if not image_files:
        print("\nไม่พบไฟล์รูปภาพในโฟลเดอร์")
        input("กด Enter เพื่อปิดโปรแกรม...")
        return
    
    print(f"\nพบรูปภาพทั้งหมด {len(image_files)} ไฟล์")
    print("กำลังเปลี่ยนชื่อไฟล์และสร้าง Screenshot...")
    
    # สร้างดิกชันนารีเพื่อเก็บจำนวนไฟล์ของแต่ละรหัสสินค้า
    product_count = {}
    success_count = 0
    screenshot_count = 0
    
    for filename in image_files:
        # ใช้ regex เพื่อหารหัสสินค้า (xx-xxxxxx)
        match = re.search(r'(\d{2}-\d{6})', filename)
        
        if match:
            product_code = match.group(1)
            
            # นับจำนวนไฟล์ของแต่ละรหัสสินค้า
            if product_code in product_count:
                product_count[product_code] += 1
                new_name = f"{product_code}_{product_count[product_code]}.jpg"
            else:
                product_count[product_code] = 1
                new_name = f"{product_code}_1.jpg"
                
            # เปลี่ยนชื่อไฟล์
            old_path = os.path.join(folder_path, filename)
            new_path = os.path.join(folder_path, new_name)
            
            try:
                os.rename(old_path, new_path)
                print(f"✓ เปลี่ยนชื่อ: {filename} -> {new_name}")
                
                # ถ้าเป็นรูปแรก (_1) ให้ทำสำเนาเพิ่มสำหรับ Screenshot
                if new_name.endswith("_1.jpg"):
                    screenshot_name = f"{product_code}.jpg"
                    screenshot_path = os.path.join(folder_path, screenshot_name)
                    shutil.copy2(new_path, screenshot_path)
                    print(f"✓ สร้าง Screenshot: {screenshot_name}")
                    screenshot_count += 1
                
                success_count += 1
            except Exception as e:
                print(f"✗ เกิดข้อผิดพลาด {filename}: {str(e)}")
        else:
            print(f"✗ ไม่พบรหัสสินค้าในชื่อไฟล์: {filename}")
    
    print(f"\nเสร็จสิ้น!")
    print(f"- เปลี่ยนชื่อสำเร็จ {success_count} ไฟล์ จากทั้งหมด {len(image_files)} ไฟล์")
    print(f"- สร้าง Screenshot สำเร็จ {screenshot_count} ไฟล์")
    input("\nกด Enter เพื่อปิดโปรแกรม...")

# เรียกใช้งานฟังก์ชัน
if __name__ == "__main__":
    rename_product_images()