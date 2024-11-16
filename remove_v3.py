import os
import re
import time

def remove_underscore_images():
    print("\n=== โปรแกรมลบรูปภาพที่มีเครื่องหมาย _ V3 ===\n")
    
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
    print("กำลังตรวจสอบและลบไฟล์...")
    
    removed_count = 0
    
    # แสดงคำเตือนและขอคำยืนยัน
    print("\n⚠️ คำเตือน: โปรแกรมจะลบไฟล์รูปภาพที่มีเครื่องหมาย _ ในชื่อไฟล์")
    confirm = input("ต้องการดำเนินการต่อหรือไม่? (y/n): ")
    
    if confirm.lower() != 'y':
        print("\nยกเลิกการทำงาน")
        input("กด Enter เพื่อปิดโปรแกรม...")
        return
    
    for filename in image_files:
        # ตรวจสอบว่ามีเครื่องหมาย _ หรือไม่
        if '_' in filename:
            try:
                file_path = os.path.join(folder_path, filename)
                os.remove(file_path)
                print(f"✓ ลบไฟล์: {filename}")
                removed_count += 1
            except Exception as e:
                print(f"✗ เกิดข้อผิดพลาดในการลบ {filename}: {str(e)}")
    
    print(f"\nเสร็จสิ้น! ลบไฟล์สำเร็จ {removed_count} ไฟล์ จากทั้งหมด {len(image_files)} ไฟล์")
    input("\nกด Enter เพื่อปิดโปรแกรม...")

# เรียกใช้งานฟังก์ชัน
if __name__ == "__main__":
    remove_underscore_images()