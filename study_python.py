# Hàm " def : define", khai báo hàm - create funtion 

# def <fintion_name>(parameter_1, parameter_2, parameter_3,, ..., ):
# Lưu trữ 1 khối lệnh để có thể tái sử dụng lại 



# def kteam():
#     print ("thu an")
#     print("ngoc thang")
# kteam()
# kteam()
# kteam()
# kteam()
# kteam()

 #nếu không có () thì nó là biến , nếu có () thì nó là hàm
# hàm coi như là 1 biến nhưng lưu trữ 1 khối lệnh , gọi lại , xài lại được 
# chỉ lấy ra giá trị chứ không gán đc


# hàm với parameter/ agrument
# Ccó bao nhiêu parammeter thì phải truyền bấy nhiêu argrument
# hàm khai báo trước , biến khai báo sau 


def caculate_fee(volume, price, percent, min_fee):  #parameter
    est_fee= volume*price*percent
    if est_fee < min_fee: 
        return min_fee
    return est_fee

def test_fee(self):
    #testcase1: fee< fee tối thiểu 
    VOLUME= 20
    PRICE=10
    PERCENT=0.00005
    MIN_FEE=60
    EXPECT_FEE= 60
    est_fee= caculate_fee(VOLUME, PRICE, PERCENT, MIN_FEE)
    self.assertEqual(est_fee,EXPECT_FEE)


def kteam(k,t,e,r):
    print(k)
    print(t,e)

lst = ['123', 'Kteam','69.96','Henrry']
kteam(*lst)







# biến cục bộ : biến đc tạo trong hàm thì ham sài, biến đc tạo trong file thì file sài, biến được tạo trong lớp thì lớp sài
# biến toàn cục: toàn bộ cục thì ở đầu sài cùng đc 

# def kteam(a,b):
#     pass
# kteam(3,'free education') # possitive argrument 

# kteam(a=3,b='free education') # key word arrgrument luôn ở sau 

    
    


    



