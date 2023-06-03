"""
N19DCCN067 - Ngô Sơn Hồng
N19DCCN070 - Lê Quang Hùng
N19DCCN112 - Nguyễn Thị Huỳnh My
"""
import math
import time
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from bisect import bisect_left

def binary_search(sorted_list, target):
    index = bisect_left(sorted_list, target)
    if index < len(sorted_list) and sorted_list[index] == target:
        return index
    return -1
def doc_file_set(duong_dan):
    with open(duong_dan, 'r') as file:
        noi_dung_file = file.read()
    noi_dung_file = noi_dung_file.lower()
    # print(noi_dung_file)
    stop_words = set(stopwords.words('english'))

    bat_dau_cau_moi = 0
    id = []
    noi_dung_stop_word = []
    for i in range(0, len(noi_dung_file)):
        if noi_dung_file[i] == "/":
            id.append(noi_dung_file[bat_dau_cau_moi:i].split()[0])
            noi_dung = set(noi_dung_file[bat_dau_cau_moi:i].split()[1:])
            bat_dau_cau_moi = i + 1
            noi_dung_stop_word.append([w for w in noi_dung if not w.lower() in stop_words])

    return noi_dung_stop_word, id
# def doc_file_list(duong_dan):
#     with open(duong_dan, 'r') as file:
#         noi_dung_file = file.read()
#     noi_dung_file = noi_dung_file.lower()
#     # print(noi_dung_file)
#     stop_words = set(stopwords.words('english'))

#     bat_dau_cau_moi = 0
#     id = []
#     noi_dung_stop_word = []
#     for i in range(0, len(noi_dung_file)):
#         if noi_dung_file[i] == "/":
#             id.append(noi_dung_file[bat_dau_cau_moi:i].split()[0])
#             noi_dung = list(noi_dung_file[bat_dau_cau_moi:i].split()[1:])
#             bat_dau_cau_moi = i + 1
#             noi_dung_stop_word.append([w for w in noi_dung if not w.lower() in stop_words])

#     return noi_dung_stop_word, id
def tao_list_tuple_tu_va_id(noi_dung_doc_text, id):
    tu_va_id = []
    for i in range(0, len(id)):
        for tu in noi_dung_doc_text[i]:
            tu_va_id.append((tu, id[i]))
    # print(tu_va_id)
    return sorted(tu_va_id, key=lambda x: x[0])
def tao_ds_tutansuatvitri(tu_va_id):
    i_vitri = 0
    tu_tansuat_vitri = []
    tan_suat_tu = 0
    tu_previuos =""
    for i in tu_va_id:
        if i[0] != tu_previuos:
            tan_suat_tu = 1
            tu_tansuat_vitri.append((i[0], tan_suat_tu, i_vitri))
            i_vitri += 1
            tu_previuos = i[0]
        else:
            tan_suat_tu += 1
            tu_tansuat_vitri[i_vitri-1] = (i[0], tan_suat_tu, i_vitri-1)
       
    return tu_tansuat_vitri
# def do_tuong_dong(tu_tansuat_vitri, noi_dung_doc_set , id_doc ,idf_url , noi_dung_truy_van , id_truy_van ):
#     f = open(idf_url, "w")
#     list_tu =[]
#     for tu in tu_tansuat_vitri:
#         list_tu.append(tu[0])
#     for i_tv in range(0,len(id_truy_van)):
#         f.write(str(id_truy_van[i_tv]) + "\n")
#         max_cos = 0
#         max_cos_doc = 0
#         for i_doc in range(0,len(id_doc)):
#             cos = 0
#             giao_doc_query=[]
#             giao_doc_query = list(set(noi_dung_doc_set[i_doc]) & set(noi_dung_truy_van[i_tv]))
#             for tu_in_giao in giao_doc_query:
#                 index =binary_search(list_tu,tu_in_giao)
#                 count_doc = noi_dung_doc_set[i_doc].count(tu_tansuat_vitri[index][0])
#                 count_truy_van = noi_dung_truy_van[i_tv].count(tu_tansuat_vitri[index][0])

#                 tf_doc = 1 + math.log10(count_doc)
#                 tf_truyvan = 1 + math.log10(count_truy_van)
#                 cos = cos + tf_doc* tf_truyvan* math.log10(int(id_doc[-1])/int(tu_tansuat_vitri[index][1])) * math.log10(int(id_doc[-1])/int(tu_tansuat_vitri[index][1]))
#             f.write(str(i_doc) + ":" + str(round(cos,2)) + " ")
#             if (cos > max_cos): 
#                 max_cos = cos
#                 max_cos_doc = i_doc
#         f.write("\n" + "Do tuong dong lon nhat - ID DOC: " + str(max_cos_doc) + "  Cos_value: " + str(round(max_cos,2)) + "\n"
#                 + "  \   " + "\n")
#     f.close() 
def mo_hinh_nhi_phan(noi_dung_truy_van,id_tv,noi_dung_docx,id_docx,tu_tansuat_vitri):
    # B1:tạo RSV ban đầu
    f = open(RSV_url, "w")
    RSV_list = []
    list_tu =[]
    for tu in tu_tansuat_vitri:
        list_tu.append(tu[0])
    for i_tv in range(0,len(id_tv)):
        f.write(str(id_tv[i_tv]) + "\n")
        RSV_list = []
        
        for i_doc in range(0,len(id_docx)):
            giao_doc_query=[]
            giao_doc_query = list(set(noi_dung_docx[i_doc]) & set(noi_dung_truy_van[i_tv]))
            rsv_value = 0
            for tu in giao_doc_query:  
                index =binary_search(list_tu,tu)
                rsv_value += math.log((len(id_docx)-tu_tansuat_vitri[index][1] + 0.5)/(tu_tansuat_vitri[index][1]+0.5))
            f.write(str(i_doc) + ":" + str(round(rsv_value,2)) + " ") 
            RSV_list.append((i_doc,rsv_value))
        f.write("\n")
        sorted_rsv = sorted(RSV_list, key=lambda x: x[1], reverse=True)
        # Lấy top 10 giá trị RSV lớn 
        top_10_rsv = sorted_rsv[:10]
        list_id_top10 = []
        for item in top_10_rsv:
            list_id_top10.append(item[0])
        # print(list_id_top10)
        rsv_result_id = []
        noidung_V = []
        id_V = []
        lanlap = 0;
        while (rsv_result_id != list_id_top10):
            lanlap+=1
            print(list_id_top10)
            rsv_result_id = list_id_top10
            for id in list_id_top10:
                noidung_V.append(noi_dung_docx[id])
                id_V.append(id)
            # print(noidung_V)
            # print(id_V)
            tu_va_id_V = tao_list_tuple_tu_va_id(noidung_V,id_V)
            tu_tansuat_vitri_V = tao_ds_tutansuatvitri(tu_va_id_V)
            list_tu_V =[]
            for tu in tu_tansuat_vitri_V:
                list_tu_V.append(tu[0])
            for i_V in range(0,len(id_V)):
                giao_V_query = []
                rsv_new_V = 0.0
                giao_V_query = giao_doc_query = list(set(noidung_V[i_V]) & set(noi_dung_truy_van[i_tv]))
                for tu in giao_V_query:
                    index_V =binary_search(list_tu_V,tu)
                    index_doc =binary_search(list_tu,tu)
                    pi = (tu_tansuat_vitri_V[index_V][1] + 0.5)/(len(id_V) + 1)
                    ri = (tu_tansuat_vitri[index_doc][1] - tu_tansuat_vitri_V[index_V][1] + 0.5)/(len(id_docx)- len(id_V) + 1)
                    print(tu)
                    print(str(tu_tansuat_vitri[index_doc][1]) + " " +str(tu_tansuat_vitri_V[index_V][1]))
                    
                    print ("pi:" + str(pi) + " ri: " + str(ri))
                    ci = math.log((pi*(1-ri)/(ri*(1 -pi))))
                    
                    rsv_new_V +=ci
                RSV_list[i_V] = (i_V,rsv_new_V)
            sorted_rsv_new = sorted(RSV_list, key=lambda x: x[1], reverse=True)
            # Lấy top 10 giá trị RSV lớn 
            top_10_rsv_new = sorted_rsv_new[:10]
            list_id_top10_new = []
            for item in top_10_rsv_new:
                list_id_top10_new.append(item[0])
            
            list_id_top10 = list_id_top10_new
            # print(tu_tansuat_vitri_V)

            # print("")
        # top_10_rsv = sorted_rsv[:10]
        print("so lan lap: " + str(lanlap))
        print(list_id_top10)
        # f.write("top 10: ")
        # ds_V = []
        # for id, rsvv in top_10_rsv:
        #     ds_V.append(noi_dung_docx[id],rsvv)
        
        # for id, rsvv in top_10_rsv:

        #     f.write(str(id) + ":" + str(round(rsvv,3))+ " ")
        # f.write("\n")

    f.close()

    
def ghi_file_tu_tansat_vitri(tu_tansaut_vitri_url ,tu_tansuat_vitri ):
    f = open(tu_tansaut_vitri_url, "w")
    for tu in tu_tansuat_vitri:
        string = str(tu[0]) + " " + str(tu[1]) + " " + str(tu[2]) + "\n"
        f.write(string)
    f.close()

def ghi_file_chi_muc_nguoc(chi_muc_nguoc_url ,chi_muc_nguoc ):
    f1 = open(chi_muc_nguoc_url, "w")
    for ids in chi_muc_nguoc:
        string = ""
        for i in range(0, len(ids)):
            if i == len(ids)-1:
                string += str(ids[i]) + "\n"
            else:
                string += str(ids[i]) + " "
        f1.write(string)
    f1.close()

if __name__ == '__main__':
    start_time = time.time()
    base_url = 'E:\A_OFFLINE_HK8\ChuyendeCNPM\IR5'
    noidung_url = base_url + '//doc-text'
    truyvan_url = base_url + '//query-text'
    RSV_url = base_url + '//rsv'
    tu_tansaut_vitri_url = base_url + '//tu_tansuat_vitri'
    print('Tách từ trong file doc-text tạo ds các từ không trùng nhau trong 1 doc')
    noi_dung_docx , id_docx = doc_file_set(noidung_url)

    print(".....")
    print('Tách từ trong danh sách query-text')
    noi_dung_truy_van, id_tv = doc_file_set(truyvan_url)

    print(".....")
    print('Tạo danh sách từ có trong file doc-text - sắp xếp')
    tu_va_id_doc = tao_list_tuple_tu_va_id(noi_dung_docx, id_docx)
    print(".....")
    print('Tạo danh sách bộ từ vựng và số doc nó xuất hiện (tansuat)')
    tu_tansuat_vitri = tao_ds_tutansuatvitri(tu_va_id_doc)

    print(".....")
    print('Đang tính.......')
    mo_hinh_nhi_phan(noi_dung_truy_van,id_tv,noi_dung_docx,id_docx,tu_tansuat_vitri)

    # print(tu_tansuat_vitri)
    # ghi_file_tu_tansat_vitri(tu_tansaut_vitri_url,tu_tansuat_vitri)


    # print(".....")
    # print('Tách các từ trong từng doc trong doc-text vẫn giữ các từ trùng trong 1 doc ')
    # noi_dung_doc_list, id_doc_list = doc_file_list(noidung_url)


    # print(".....")
    # print('Tách từ trong danh sách query-text')
    # # noi_dung_truy_van_list, id_tv_list = doc_file_list(truyvan_url)


    # print(".....")
    # print('Đang tính độ tương đồng.......')
    # do_tuong_dong(tu_tansuat_vitri , noi_dung_doc_list, id_doc_list, idf_url ,noi_dung_truy_van_list,id_tv_list)
    
    print('Hoàn thành chương trình!')
    end_time = time.time()
    total_time = end_time - start_time
    print(f"Thời gian chạy chương trình: {total_time} giây")

    
