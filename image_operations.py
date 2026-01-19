import cv2
import numpy as np

def create_sample_image():
    """创建一个示例图像"""
    img = np.zeros((400, 600, 3), dtype=np.uint8)
    
    # 画一个绿色矩形
    cv2.rectangle(img, (50, 50), (200, 200), (0, 255, 0), -1)
    
    # 画一个红色圆形
    cv2.circle(img, (400, 200), 80, (0, 0, 255), -1)
    
    # 添加文字
    cv2.putText(img, 'OpenCV Demo', (200, 350), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    
    return img

def convert_to_grayscale(image):
    """将彩色图像转换为灰度图"""
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

if __name__ == "__main__":
    image = create_sample_image()
    
    # 保存彩色图像
    cv2.imwrite("sample_output_color.jpg", image)
    print("彩色图像已保存为 'sample_output_color.jpg'")
    
    # 转换为灰度并保存
    gray_image = convert_to_grayscale(image)
    cv2.imwrite("sample_output_gray.jpg", gray_image)
    print("灰度图像已保存为 'sample_output_gray.jpg'")
    
    print("程序执行完成！")