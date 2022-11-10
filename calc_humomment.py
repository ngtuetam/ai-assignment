from proccess_image import convert_to_bin
import cv2
import numpy as np

# tính các moment HU s1,s2
def caculate_HuMM(src):
    # tính các moment trung tâm chuẩn hóa M02,M20, M11
    def calculateMomentStand(p, q, mpq, m00):
        M_pq = (mpq)/(m00 ** (((p+q)/2)+1))
        M_pq = np.round_(M_pq, 2)
        return M_pq
    
    img = cv2.imread(src)
    img = convert_to_bin(img)
    #print(img.shape)
    img = np.round_(img)
    row, col, high = img.shape
    sum = 0
    def calculateMoment(p, q):
        m_pq = 0
        for r in range(row):
            for c in range(col):
                m_pq = m_pq + ((r - x_bar)**p)*((c-y_bar)**q)*(img[r][c][0])
        return m_pq
    for r in range(row):
        for c in range(col):
            if (img[r][c][0] == 1):
                sum = sum + 1
    # diện tích của đối tượng m00
    m00 = sum
    #print("dien tich cua doi tuong", m00)
    # tính tọa độ trọng tâm của đối tượng : x_bar, y_bar
    sumX = 0
    sumY = 0
    for r in range(row):
        for c in range(col):
            sumX = sumX + c*(img[r][c][0])
            sumY = sumY + r*(img[r][c][0])
    x_bar = sumX/m00
    x_bar = np.round_(x_bar, 2)
    y_bar = sumY/m00
    y_bar = np.round_(y_bar, 2)
    #print("toa do trong tam cua doi tuong")
    #print("x_bar: ", x_bar)
    #print("y_bar: ", y_bar)
    # các moment trung tâm m02,m20,m11



    m02 = calculateMoment(0, 2)
    #print("gia tri m02", m02)
    m20 = calculateMoment(2, 0)
    #print("gia tri m20", m20)
    m11 = calculateMoment(1, 1)
    #print("gia tri m11", m11)
    m12 = calculateMoment(1, 2)
    #print("gia tri m12", m12)
    m21 = calculateMoment(2, 1)
    #print("gia tri m21", m21)
    m03 = calculateMoment(0, 3)
    #print("gia tri m30", m03)
    m30 = calculateMoment(3, 0)
    #print("gia tri m30", m30)



    M02 = calculateMomentStand(0, 2, m02, m00)
    #print("gia tri M02", M02)
    M20 = calculateMomentStand(2, 0, m20, m00)
    #print("gia tri M20", M20)
    M11 = calculateMomentStand(1, 1, m11, m00)
    #print("gia tri M11", M11)
    #
    M12 = calculateMomentStand(1, 2, m12, m00)
    #print("gia tri M02", M12)
    M21 = calculateMomentStand(2, 1, m21, m00)
    #print("gia tri M20", M21)
    M30 = calculateMomentStand(3, 0, m30, m00)
    #print("gia tri M11", M30)
    M03 = calculateMomentStand(0, 3, m03, m00)
    #print("gia tri M11", M30)

    
    
    S1 = M02+M20
    S2 = (M20 - M02)*(M20+M02)+4*M11*M11
    S3 = ((M30 - 3*M12)**2)+((M30-3*M21)**2)
    S4 = ((M30 + M12)**2)+((M03 + M21)**2)
    S5 = (M30 - 3*M12)*(M30+M12)*(((M30+M12)**2)-3*((M03+M21)**2)) + (3*M21 - M03)*(M03+M21)*(3*((M30+M12)**2)-(M03 + M21)**2)
    S6 = (M20 - M02)*(((M30 + M12)**2)-((M03 + M21)**2)) + 4*M11*(M30 + M12)*(M03 + M21)
    S7 = (3*M21 - M03)*(M30+M12)*(((M30+M12)**2)-3*((M03+M21)**2)) + (M30-3*M12)**2*(M21+M02)*((3*(M30+M12)**2)-((M03+M21)**2))
    #print("S1", S1)
    #print("S2", S2)
    #print("S3", S3)
    #print("S4", S4)
    #print("S5", S5)
    #print("S5", S6)
    #print("S7", S7)
    res = []
    res.append(S1)
    res.append(S2)
    res.append(S3)
    res.append(S4)
    res.append(S5)
    res.append(S6)
    res.append(S7)
    return res        

# if __name__ == "__main__":
#     res = caculate_HuMM('/gray_img/tomato/tomato gray 2.jpg')
    # for i in res:
        #print(i)     

# if __name__ == "__main__":
#     res = caculate_HuMM('/home/ngtuetam/workspace/ai_assign/bin_images/orange_bin/*.jpg')
#     print(res)