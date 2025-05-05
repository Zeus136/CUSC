import pandas as pd

# Dữ liệu mẫu
data = {
    "icd_code": [
        "J00", "E11", "I10", "J45", "M54.5", "F32", "L20", "B20", "J10", "I25", 
        "F41", "C50", "A15", "N40", "M16", "I20", "I63", "L40", "M17", "D63"
    ],
    "disease_name": [
        "Cảm lạnh", "Tiểu đường type 2", "Tăng huyết áp", "Hen suyễn", "Đau lưng giữa", 
        "Trầm cảm", "Viêm da cơ địa", "HIV/AIDS", "Cảm cúm", "Bệnh tim mạch",
        "Lo âu", "Ung thư vú", "Viêm phổi", "Phì đại tuyến tiền liệt", "Thoái hóa khớp",
        "Đau thắt ngực", "Tai biến mạch máu não", "Vẩy nến", "Thoái hóa khớp gối", "Thiếu máu"
    ],
    "symptoms": [
        "Sổ mũi, ho, đau họng", "Mệt mỏi, khát nước nhiều, tiểu nhiều", "Đau đầu, chóng mặt, mệt mỏi", 
        "Khó thở, thở rít, ho, cảm giác nặng ngực", "Đau vùng lưng, hạn chế cử động", "Buồn bã, mất ngủ, mệt mỏi, suy giảm năng lượng", 
        "Ngứa, đỏ da, khô da, vết lở loét", "Sụt cân, mệt mỏi, sốt, nhiễm trùng tái phát", "Sổ mũi, đau họng, ho", 
        "Đau ngực, khó thở, mệt mỏi", "Lo lắng, tim đập nhanh, mất ngủ", "Khối u ở vú, đau, thay đổi hình dáng", 
        "Ho, sốt, mệt mỏi, khó thở", "Đi tiểu nhiều, tiểu đêm", "Đau khớp, khó cử động", "Đau thắt ngực, khó thở", 
        "Đau đầu, tê tay, yếu chân", "Ngứa, da bong tróc, vảy trắng", "Đau khớp gối, cứng khớp", "Mệt mỏi, da nhợt nhạt"
    ],
    "treatment_regimen": [
        "Thuốc giảm đau, thuốc ho", "Metformin, insulin", "Thuốc ức chế ACE, thuốc lợi tiểu", 
        "Inhaled corticosteroids, beta agonists", "Thuốc giảm đau, vật lý trị liệu", "Thuốc chống trầm cảm, liệu pháp tâm lý", 
        "Kem steroid, kem dưỡng ẩm", "ARV (Antiretroviral therapy)", "Thuốc giảm đau, thuốc kháng sinh", 
        "Thuốc hạ huyết áp, thuốc chống đông máu", "Thuốc an thần, thuốc giảm lo âu", "Phẫu thuật, hóa trị", 
        "Kháng sinh, thuốc giảm ho, nghỉ ngơi", "Thuốc giảm tiểu, thuốc điều trị tuyến tiền liệt", "Thuốc giảm đau, vật lý trị liệu", 
        "Thuốc chống đông máu, thuốc giảm đau", "Kháng sinh, thuốc điều trị tai biến", "Thuốc giảm ngứa, thuốc điều trị vẩy nến", 
        "Thuốc giảm đau, thuốc chống viêm", "Thuốc bổ máu, điều trị nguyên nhân thiếu máu"
    ],
    "treatment_type": [
        "Medication", "Medication", "Medication", "Medication", "Medication, Therapy", "Medication, Therapy", 
        "Medication", "Medication", "Medication", "Medication", "Medication", "Surgery, Medication", "Medication", 
        "Medication", "Medication", "Medication", "Medication", "Medication", "Medication", "Medication"
    ],
    "severity": [
        "Mild", "Severe", "Moderate", "Moderate", "Moderate", "Severe", "Mild", "Severe", "Mild", 
        "Severe", "Moderate", "Severe", "Severe", "Moderate", "Moderate", "Moderate", "Severe", "Mild", 
        "Moderate", "Moderate"
    ],
    "treatment_duration": [
        "1 tuần", "Ongoing", "Ongoing", "2 tuần", "3 tuần", "6 tháng", "2 tuần", "Ongoing", "1 tuần", 
        "Ongoing", "2 tuần", "6 tháng", "Ongoing", "2 tuần", "3 tuần", "1 tháng", "Ongoing", "2 tuần", 
        "1 tháng", "2 tháng"
    ],
    "side_effects": [
        "Không có", "Đau bụng, buồn nôn", "Ho, chóng mặt", "Khó thở, ho, kích ứng mũi", "Đau cơ, cứng cơ", 
        "Tăng cân, buồn nôn", "Da khô, kích ứng da", "Đau đầu, buồn nôn", "Sổ mũi, buồn nôn", "Mệt mỏi, buồn nôn", 
        "Khó ngủ, mệt mỏi", "Chóng mặt, mệt mỏi", "Mệt mỏi, khó thở", "Mệt mỏi, khó chịu", "Đau cơ, mệt mỏi", 
        "Chóng mặt, buồn nôn", "Đau đầu, mệt mỏi", "Đau, chóng mặt", "Mệt mỏi, da tái", "Không có"
    ],
    "comorbidities": [
        "Không có", "Tăng huyết áp", "Bệnh tim", "Dị ứng", "Không có", "Không có", "Dị ứng", "Tăng huyết áp", 
        "Bệnh tim", "Không có", "Lo âu", "Dị ứng", "Không có", "Tiểu đường", "Thừa cân", "Hút thuốc", "Tiểu đường", 
        "Không có", "Dị ứng", "Tăng huyết áp"
    ],
    "data_source": [
        "WHO database", "Clinical trials", "Hospital records", "Medical articles", "Hospital database", "WHO database", 
        "Clinical guidelines", "Hospital records", "WHO database", "Clinical trials", "Hospital records", "Clinical trials", 
        "Medical articles", "Hospital records", "Hospital records", "Clinical guidelines", "Hospital records", 
        "WHO database", "Clinical guidelines", "Clinical trials"
    ]
}

# Tạo DataFrame từ dữ liệu
df = pd.DataFrame(data)

# Ghi dữ liệu vào file Excel
output_file = "data.xlsx"
df.to_excel(output_file, index=False)

print(f"File Excel đã được tạo: {output_file}")