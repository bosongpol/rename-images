import os
import re
import time

def rename_product_images():
    print("\n=== โปรแกรมเปลี่ยนชื่อรูปภาพสินค้า V2 ===\n")
    
    # ให้ผู้ใช้ป้อนพาธของโฟลเดอร์
    print("กรุณาลากโฟลเดอร์ที่มีรูปภาพมาวางที่นี่ แล้วกด Enter:")
    folder_path = input().strip('"')  # ลบเครื่องหมาย " ออก
    
    if not os.path.exists(folder_path):
        print("\nไม่พบโฟลเดอร์ที่ระบุ กรุณาตรวจสอบอีกครั้ง")
        input("กด Enter เพื่อปิดโปรแกรม...")
        return
    
    # รวบรวมไฟล์ทั้งหมดในโฟลเดอร์
    files = os.listdir(folder_path)
    
    # กรองเฉพาะไฟล์รูปภาพ (รองรับทั้งตัวพิมพ์เล็กและใหญ่)
    image_extensions = ('.jpg', '.jpeg', '.png', '.JPG', '.JPEG', '.PNG')
    image_files = [f for f in files if f.endswith(image_extensions)]
    
    if not image_files:
        print("\nไม่พบไฟล์รูปภาพในโฟลเดอร์")
        input("กด Enter เพื่อปิดโปรแกรม...")
        return
    
    print(f"\nพบรูปภาพทั้งหมด {len(image_files)} ไฟล์")
    print("กำลังเปลี่ยนชื่อไฟล์...")
    
    # สร้างดิกชันนารีเพื่อเก็บจำนวนไฟล์ของแต่ละรหัสสินค้า
    product_count = {}
    success_count = 0
    failed_files = []  # เก็บรายการไฟล์ที่มีปัญหา
    
    for filename in image_files:
        # ตัดส่วนที่อยู่หลังจุดแรกออก (ยกเว้นนามสกุลไฟล์)
        base_name = filename
        if '.' in filename[:-4]:  # ตรวจสอบว่ามีจุดก่อนนามสกุลไฟล์หรือไม่
            base_name = filename.split('.')[0]  # เอาเฉพาะส่วนก่อนจุดแรก
        
        # ใช้ regex เพื่อหารหัสสินค้า (รองรับทลายรูปแบบ)
        match = re.search(r'@?(\d{6}-\d{4}|\d{2,3}-\d{5,6})', base_name)
        
        if match:
            product_code = match.group(1)  # ใช้ group(1) เพื่อเอาเฉพาะตัวเลข
            
            # นับจำนวนไฟล์ของแต่ละรหัสสินค้า
            if product_code in product_count:
                product_count[product_code] += 1
                new_name = f"{product_code}_{product_count[product_code]}.jpg"
            else:
                product_count[product_code] = 1
                new_name = f"{product_code}.jpg"  # ไม่ใส่ _1 สำหรับภาพแรก
                
            # เปลี่ยนชื่อไฟล์
            old_path = os.path.join(folder_path, filename)
            new_path = os.path.join(folder_path, new_name)
            
            try:
                os.rename(old_path, new_path)
                print(f"✓ เปลี่ยนชื่อ: {filename} -> {new_name}")
                success_count += 1
            except Exception as e:
                error_msg = f"✗ เกิดข้อผิดพลาด {filename}: {str(e)}"
                print(error_msg)
                failed_files.append((filename, "ไม่สามารถเปลี่ยนชื่อได้", str(e)))
        else:
            error_msg = f"✗ ไม่พบรหัสสินค้า (xx-xxxxxx) ในชื่อไฟล์: {filename}"
            print(error_msg)
            failed_files.append((filename, "ไม่พบรหัสสินค้า", "-"))
    
    print(f"\nเสร็จสิ้น! เปลี่ยนชื่อสำเร็จ {success_count} ไฟล์ จากทั้งหมด {len(image_files)} ไฟล์")
    
    # แสดงรายการไฟล์ที่มีปัญหาทั้งหมด
    if failed_files:
        print("\nรายการไฟล์ที่ไม่สามารถเปลี่ยนชื่อได้:")
        print("-" * 80)
        for file, reason, error in failed_files:
            print(f"ไฟล์: {file}")
            print(f"สาเหตุ: {reason}")
            if error != "-":
                print(f"ข้อผิดพลาด: {error}")
            print("-" * 80)
    
    input("\nกด Enter เพื่อปิดโปรแกรม...")

# เรียกใช้งานฟังก์ชัน
if __name__ == "__main__":
    rename_product_images()

