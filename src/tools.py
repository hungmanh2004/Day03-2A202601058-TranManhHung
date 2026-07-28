"""
🛠️ TOOL REGISTRY & SCHEMAS (Dành cho Role 2: Tool & Spec Engineer)
Chủ đề: Agent Chatbot Định Hướng Sự Nghiệp

Bộ 5 tool lõi cho luồng ReAct:
    assess_user_profile -> search_careers -> get_career_details
    -> analyze_skill_gap -> recommend_learning_path

Toàn bộ dữ liệu (nghề nghiệp, khóa học) là dữ liệu GIẢ LẬP (mock),
giúp bài lab chạy ổn định, không phụ thuộc Internet hay API bên ngoài.
"""

from typing import List, Dict, Any, Union


# ============================================================
# 📦 MOCK DATABASE
# ============================================================

CAREER_DATABASE: Dict[str, Dict[str, Any]] = {
    "data_analyst": {
        "name": "Chuyên viên Phân tích Dữ liệu (Data Analyst)",
        "field": "Công nghệ / Dữ liệu",
        "aliases": ["data analyst", "phân tích dữ liệu", "chuyên viên phân tích dữ liệu"],
        "description": "Thu thập, xử lý và phân tích dữ liệu để hỗ trợ ra quyết định kinh doanh.",
        "tasks": [
            "Làm sạch và xử lý dữ liệu thô",
            "Xây dựng báo cáo, dashboard trực quan",
            "Phát hiện xu hướng và insight từ dữ liệu",
            "Phối hợp với các phòng ban để đề xuất giải pháp dựa trên dữ liệu",
        ],
        "requirements": [
            "Tốt nghiệp CNTT, Toán, Thống kê hoặc ngành liên quan",
            "Tư duy logic, cẩn thận, khả năng làm việc với số liệu",
        ],
        "environment": "Văn phòng, làm việc theo nhóm với phòng Kinh doanh/Vận hành, có thể làm từ xa.",
        "required_skills": ["Python", "SQL", "Excel", "Thống kê", "Trực quan hóa dữ liệu"],
        "related_interests": ["dữ liệu", "phân tích", "công nghệ", "logic", "số liệu", "toán học"],
    },
    "software_developer": {
        "name": "Lập trình viên Phần mềm (Software Developer)",
        "field": "Công nghệ / Kỹ thuật",
        "aliases": ["software developer", "lập trình viên", "developer", "kỹ sư phần mềm"],
        "description": "Thiết kế, xây dựng và bảo trì các ứng dụng, hệ thống phần mềm.",
        "tasks": [
            "Viết và kiểm thử mã nguồn",
            "Thiết kế kiến trúc hệ thống",
            "Sửa lỗi và tối ưu hiệu năng",
            "Phối hợp với team sản phẩm để triển khai tính năng mới",
        ],
        "requirements": [
            "Tốt nghiệp CNTT, Khoa học máy tính hoặc tương đương",
            "Kỹ năng giải quyết vấn đề, tư duy thuật toán",
        ],
        "environment": "Văn phòng công nghệ hoặc làm việc từ xa, mô hình Agile/Scrum.",
        "required_skills": ["Python", "JavaScript", "Git", "Cấu trúc dữ liệu & giải thuật", "Cơ sở dữ liệu"],
        "related_interests": ["lập trình", "công nghệ", "logic", "giải thuật", "sáng tạo kỹ thuật"],
    },
    "data_scientist": {
        "name": "Nhà Khoa học Dữ liệu (Data Scientist)",
        "field": "Công nghệ / Dữ liệu",
        "aliases": ["data scientist", "khoa học dữ liệu"],
        "description": "Xây dựng mô hình dự đoán, ứng dụng machine learning để giải quyết bài toán kinh doanh.",
        "tasks": [
            "Xây dựng và huấn luyện mô hình Machine Learning",
            "Thử nghiệm A/B và đánh giá mô hình",
            "Làm việc với dữ liệu lớn (Big Data)",
            "Trình bày kết quả cho các bên liên quan",
        ],
        "requirements": [
            "Tốt nghiệp Toán, Thống kê, CNTT hoặc ngành liên quan",
            "Nền tảng vững về xác suất thống kê và lập trình",
        ],
        "environment": "Văn phòng công nghệ, làm việc chặt chẽ với đội kỹ thuật và sản phẩm.",
        "required_skills": ["Python", "Machine Learning", "Thống kê", "SQL", "Trực quan hóa dữ liệu"],
        "related_interests": ["dữ liệu", "trí tuệ nhân tạo", "toán học", "nghiên cứu", "công nghệ"],
    },
    "ux_ui_designer": {
        "name": "Nhà Thiết kế UX/UI (UX/UI Designer)",
        "field": "Thiết kế / Sáng tạo",
        "aliases": ["ux/ui designer", "thiết kế ux", "thiết kế ui", "nhà thiết kế trải nghiệm người dùng"],
        "description": "Thiết kế giao diện và trải nghiệm người dùng cho sản phẩm số.",
        "tasks": [
            "Nghiên cứu hành vi và nhu cầu người dùng",
            "Vẽ wireframe, prototype giao diện",
            "Thiết kế UI chi tiết trên Figma",
            "Kiểm thử trải nghiệm người dùng (usability testing)",
        ],
        "requirements": [
            "Có tư duy thẩm mỹ và sự đồng cảm với người dùng",
            "Không bắt buộc bằng cấp cụ thể, ưu tiên portfolio",
        ],
        "environment": "Văn phòng công nghệ/sáng tạo, phối hợp chặt chẽ với đội sản phẩm và kỹ thuật.",
        "required_skills": ["Figma", "Thiết kế UI/UX", "Nghiên cứu người dùng", "Tư duy thẩm mỹ"],
        "related_interests": ["thiết kế", "sáng tạo", "mỹ thuật", "hình ảnh", "trải nghiệm người dùng"],
    },
    "digital_marketing": {
        "name": "Chuyên viên Marketing Số (Digital Marketing)",
        "field": "Kinh doanh / Marketing",
        "aliases": ["digital marketing", "marketing số", "chuyên viên marketing"],
        "description": "Lập kế hoạch và triển khai các chiến dịch tiếp thị trên nền tảng số.",
        "tasks": [
            "Xây dựng chiến lược nội dung và quảng cáo",
            "Tối ưu SEO/SEM",
            "Phân tích hiệu quả chiến dịch",
            "Quản lý các kênh mạng xã hội",
        ],
        "requirements": [
            "Tốt nghiệp Marketing, Truyền thông hoặc ngành liên quan",
            "Khả năng sáng tạo nội dung và nhạy bén xu hướng",
        ],
        "environment": "Văn phòng, làm việc theo chiến dịch, thường xuyên có deadline gấp.",
        "required_skills": ["SEO", "Content Marketing", "Phân tích dữ liệu cơ bản", "Giao tiếp", "Quảng cáo số (Ads)"],
        "related_interests": ["marketing", "truyền thông", "sáng tạo nội dung", "kinh doanh", "mạng xã hội"],
    },
    "business_analyst": {
        "name": "Chuyên viên Phân tích Nghiệp vụ (Business Analyst)",
        "field": "Kinh doanh / Quản lý",
        "aliases": ["business analyst", "phân tích nghiệp vụ", "ba"],
        "description": "Phân tích quy trình nghiệp vụ, kết nối nhu cầu kinh doanh với giải pháp công nghệ.",
        "tasks": [
            "Thu thập và phân tích yêu cầu nghiệp vụ",
            "Vẽ sơ đồ quy trình (process flow)",
            "Viết tài liệu đặc tả yêu cầu (BRD/SRS)",
            "Phối hợp giữa bộ phận kinh doanh và đội kỹ thuật",
        ],
        "requirements": [
            "Tốt nghiệp Kinh tế, Quản trị kinh doanh, CNTT hoặc liên quan",
            "Kỹ năng giao tiếp và tư duy hệ thống tốt",
        ],
        "environment": "Văn phòng, làm việc liên phòng ban, thường xuyên họp và trình bày.",
        "required_skills": ["Phân tích nghiệp vụ", "Giao tiếp", "Excel", "Quản lý dự án", "SQL cơ bản"],
        "related_interests": ["kinh doanh", "quản lý", "logic", "giao tiếp", "quy trình"],
    },
}


SKILL_COURSE_MAP: Dict[str, Dict[str, Any]] = {
    "python": {"course": "Python for Data Analysis (Coursera/Udemy)", "hours": 40},
    "sql": {"course": "SQL cơ bản đến nâng cao (DataCamp)", "hours": 25},
    "excel": {"course": "Excel cho phân tích dữ liệu (Udemy)", "hours": 15},
    "thống kê": {"course": "Nhập môn Thống kê ứng dụng (Coursera)", "hours": 30},
    "trực quan hóa dữ liệu": {"course": "Power BI/Tableau từ cơ bản đến nâng cao", "hours": 20},
    "machine learning": {"course": "Machine Learning Specialization (Andrew Ng)", "hours": 60},
    "javascript": {"course": "JavaScript cơ bản đến nâng cao (freeCodeCamp)", "hours": 35},
    "git": {"course": "Git & GitHub cho người mới bắt đầu", "hours": 10},
    "cấu trúc dữ liệu & giải thuật": {"course": "Data Structures & Algorithms (Udemy)", "hours": 50},
    "cơ sở dữ liệu": {"course": "Nhập môn Cơ sở dữ liệu (SQL/NoSQL)", "hours": 25},
    "figma": {"course": "Thiết kế UI với Figma từ A-Z", "hours": 20},
    "thiết kế ui/ux": {"course": "UX/UI Design Fundamentals", "hours": 40},
    "nghiên cứu người dùng": {"course": "User Research Methods", "hours": 15},
    "seo": {"course": "SEO Fundamentals (Google/HubSpot Academy)", "hours": 15},
    "content marketing": {"course": "Content Marketing Certification (HubSpot)", "hours": 20},
    "quảng cáo số (ads)": {"course": "Google Ads & Facebook Ads cơ bản", "hours": 20},
    "phân tích nghiệp vụ": {"course": "Business Analysis Fundamentals (IIBA)", "hours": 30},
    "quản lý dự án": {"course": "Quản lý dự án cơ bản (PMI/Coursera)", "hours": 25},
    "giao tiếp": {"course": "Kỹ năng giao tiếp và thuyết trình hiệu quả", "hours": 10},
}


# ============================================================
# 🔧 HELPER (nội bộ, không đăng ký làm tool)
# ============================================================

def _find_career(query: str) -> Union[str, None]:
    """Tìm mã (key) nghề nghiệp trong CAREER_DATABASE theo tên/mã/alias, không phân biệt hoa thường."""
    if not isinstance(query, str) or not query.strip():
        return None

    q = query.strip().lower()
    for code, info in CAREER_DATABASE.items():
        if q == code or q == info["name"].lower() or q in info.get("aliases", []):
            return code
    for code, info in CAREER_DATABASE.items():
        if q in info["name"].lower() or q in code or any(q in a for a in info.get("aliases", [])):
            return code
    return None


def _error(message: str) -> str:
    """Trả về chuỗi thông báo lỗi chuẩn hóa."""
    return f"LỖI: {message}"


# ============================================================
# 🛠️ 5 TOOL CHÍNH
# ============================================================

def assess_user_profile(profile: Dict[str, Any]) -> Dict[str, Any]:
    """
    Phân tích học vấn, kỹ năng, sở thích, tính cách và mục tiêu để tạo hồ sơ nghề nghiệp chuẩn hóa.
    """
    try:
        if not isinstance(profile, dict):
            return {"error": _error("profile must be a dictionary")}

        education = profile.get("education", "Chưa cung cấp")
        raw_skills = profile.get("skills", [])
        raw_interests = profile.get("interests", [])
        personality = profile.get("personality", "Chưa cung cấp")
        goals = profile.get("goals", "Chưa cung cấp")

        if not isinstance(raw_skills, list):
            raw_skills = [raw_skills]
        if not isinstance(raw_interests, list):
            raw_interests = [raw_interests]

        normalized_skills = [str(s).strip().title() for s in raw_skills if str(s).strip()]
        normalized_interests = [str(i).strip().title() for i in raw_interests if str(i).strip()]

        FIELD_KEYWORDS = {
            "Công nghệ / Dữ liệu": ["python", "sql", "dữ liệu", "lập trình", "logic", "công nghệ", "toán", "excel", "phân tích", "thuật toán"],
            "Thiết kế / Sáng tạo": ["thiết kế", "vẽ", "sáng tạo", "mỹ thuật", "hình ảnh", "figma", "ui", "ux", "trải nghiệm"],
            "Kinh doanh / Marketing": ["kinh doanh", "marketing", "bán hàng", "giao tiếp", "thuyết trình", "seo", "truyền thông", "quảng cáo"],
            "Quản lý / Vận hành": ["quản lý", "lãnh đạo", "tổ chức", "lập kế hoạch", "dự án", "quy trình"],
        }

        combined_text = " ".join(normalized_skills + normalized_interests).lower()
        field_scores = {
            field: sum(1 for kw in keywords if kw in combined_text)
            for field, keywords in FIELD_KEYWORDS.items()
        }
        field_scores = {f: s for f, s in field_scores.items() if s > 0}
        suggested_fields = sorted(field_scores, key=field_scores.get, reverse=True)[:3]
        if not suggested_fields:
            suggested_fields = ["Chưa xác định rõ - cần bổ sung thêm sở thích/kỹ năng"]

        return {
            "education": education,
            "normalized_skills": normalized_skills,
            "normalized_interests": normalized_interests,
            "personality": personality,
            "career_goals": goals,
            "suggested_fields": suggested_fields,
            "profile_summary": (
                f"Người dùng có nền tảng '{education}', sở hữu {len(normalized_skills)} kỹ năng, "
                f"quan tâm đến {len(normalized_interests)} lĩnh vực. "
                f"Định hướng phù hợp: {', '.join(suggested_fields)}."
            ),
        }
    except Exception as exc:
        return {"error": _error(str(exc))}


def search_careers(interests: List[str], skills: List[str]) -> List[Dict[str, Any]]:
    """
    Tìm các nghề phù hợp dựa trên sở thích và kỹ năng, có tính điểm mức độ phù hợp sơ bộ (match_score).
    """
    try:
        if not isinstance(interests, list):
            interests = [interests] if interests is not None else []
        if not isinstance(skills, list):
            skills = [skills] if skills is not None else []

        interests_lower = [str(i).strip().lower() for i in interests if str(i).strip()]
        skills_lower = [str(s).strip().lower() for s in skills if str(s).strip()]

        results = []
        for code, info in CAREER_DATABASE.items():
            matched_interests = {
                i for i in interests_lower
                if any(i in kw or kw in i for kw in info["related_interests"])
            }
            matched_skills = {
                s for s in skills_lower
                if any(s in rs.lower() or rs.lower() in s for rs in info["required_skills"])
            }
            score = len(matched_interests) * 2 + len(matched_skills) * 3

            if score > 0:
                reason_parts = []
                if matched_interests:
                    reason_parts.append(f"phù hợp sở thích: {', '.join(matched_interests)}")
                if matched_skills:
                    reason_parts.append(f"có sẵn kỹ năng: {', '.join(matched_skills)}")
                results.append({
                    "career_code": code,
                    "career_name": info["name"],
                    "field": info["field"],
                    "match_score": score,
                    "reason": "; ".join(reason_parts),
                })

        results.sort(key=lambda x: x["match_score"], reverse=True)

        if not results:
            return [{
                "career_code": None,
                "career_name": "Không tìm thấy nghề phù hợp",
                "field": None,
                "match_score": 0,
                "reason": "Không có sở thích/kỹ năng nào khớp với dữ liệu hiện có. Hãy thử bổ sung thêm từ khóa.",
            }]

        return results
    except Exception as exc:
        return [{"error": _error(str(exc))}]


def get_career_details(career_name: str) -> Union[Dict[str, Any], str]:
    """
    Tra cứu nhiệm vụ, yêu cầu và môi trường làm việc chi tiết của một nghề.
    """
    try:
        if not isinstance(career_name, str) or not career_name.strip():
            return _error("career_name is required")

        code = _find_career(career_name)
        if code is None:
            return _error(f"Không tìm thấy thông tin nghề nghiệp cho '{career_name}'.")

        info = CAREER_DATABASE[code]
        return {
            "career_code": code,
            "career_name": info["name"],
            "field": info["field"],
            "description": info["description"],
            "tasks": info["tasks"],
            "requirements": info["requirements"],
            "environment": info["environment"],
            "required_skills": info["required_skills"],
        }
    except Exception as exc:
        return _error(str(exc))


def analyze_skill_gap(user_skills: List[str], target_career: str) -> Union[Dict[str, Any], str]:
    """
    So sánh kỹ năng hiện có của người dùng với yêu cầu kỹ năng của nghề mục tiêu.
    """
    try:
        if not isinstance(user_skills, list):
            user_skills = [user_skills] if user_skills is not None else []
        if not isinstance(target_career, str) or not target_career.strip():
            return _error("target_career is required")

        code = _find_career(target_career)
        if code is None:
            return _error(f"Không tìm thấy nghề '{target_career}' để phân tích khoảng cách kỹ năng.")

        info = CAREER_DATABASE[code]
        required_skills = info["required_skills"]
        user_skills_lower = [str(s).strip().lower() for s in user_skills if str(s).strip()]

        matched_skills = [
            rs for rs in required_skills
            if any(rs.lower() in us or us in rs.lower() for us in user_skills_lower)
        ]
        missing_skills = [rs for rs in required_skills if rs not in matched_skills]
        match_percentage = round(len(matched_skills) / len(required_skills) * 100, 1) if required_skills else 0.0

        return {
            "career_code": code,
            "career_name": info["name"],
            "matched_skills": matched_skills,
            "missing_skills": missing_skills,
            "match_percentage": match_percentage,
            "summary": (
                f"Bạn đã đáp ứng {len(matched_skills)}/{len(required_skills)} kỹ năng yêu cầu "
                f"cho nghề '{info['name']}' (đạt {match_percentage}%)."
            ),
        }
    except Exception as exc:
        return _error(str(exc))


def recommend_learning_path(missing_skills: List[str], duration_months: int) -> Dict[str, Any]:
    """
    Tạo lộ trình học theo giai đoạn để bù đắp các kỹ năng còn thiếu.
    """
    try:
        if not isinstance(missing_skills, list):
            missing_skills = [missing_skills] if missing_skills is not None else []

        try:
            duration_value = int(duration_months)
        except (TypeError, ValueError):
            return {"error": _error("duration_months must be an integer")}

        if not missing_skills:
            return {
                "duration_months": duration_value,
                "phases": [],
                "note": "Bạn đã đáp ứng đủ kỹ năng yêu cầu! Có thể tập trung làm dự án thực tế hoặc luyện phỏng vấn.",
            }

        if duration_value >= 6:
            phase_names = ["Nền tảng", "Nâng cao", "Ứng dụng thực tế"]
        elif duration_value >= 3:
            phase_names = ["Nền tảng", "Ứng dụng thực tế"]
        else:
            phase_names = ["Tập trung cấp tốc"]

        num_phases = len(phase_names)
        base_months = duration_value // num_phases
        remainder = duration_value % num_phases
        months_per_phase = [base_months + (1 if i < remainder else 0) for i in range(num_phases)]

        skills_per_phase: List[List[str]] = [[] for _ in range(num_phases)]
        for idx, skill in enumerate(missing_skills):
            skills_per_phase[idx % num_phases].append(str(skill))

        phases = []
        for i, phase_name in enumerate(phase_names):
            phase_skills = skills_per_phase[i]
            courses = []
            for skill in phase_skills:
                course_info = SKILL_COURSE_MAP.get(skill.strip().lower())
                if course_info:
                    courses.append({
                        "skill": skill,
                        "suggested_course": course_info["course"],
                        "estimated_hours": course_info["hours"],
                    })
                else:
                    courses.append({
                        "skill": skill,
                        "suggested_course": f"Khóa học online cơ bản về '{skill}' (chưa có dữ liệu cụ thể)",
                        "estimated_hours": 20,
                    })

            phases.append({
                "phase_name": phase_name,
                "duration_months": months_per_phase[i],
                "skills_to_learn": phase_skills,
                "courses": courses,
            })

        return {
            "duration_months": duration_value,
            "total_missing_skills": len(missing_skills),
            "phases": phases,
            "note": f"Lộ trình được chia thành {num_phases} giai đoạn trong {duration_value} tháng.",
        }
    except Exception as exc:
        return {"error": _error(str(exc))}


# ============================================================
# 📋 ĐĂNG KÝ TOOL CHO REACT AGENT
# ============================================================

AVAILABLE_TOOLS = {
    "assess_user_profile": assess_user_profile,
    "search_careers": search_careers,
    "get_career_details": get_career_details,
    "analyze_skill_gap": analyze_skill_gap,
    "recommend_learning_path": recommend_learning_path,
}


# ============================================================
# ▶️ DEMO: minh họa luồng ReAct tiêu biểu
# ============================================================

if __name__ == "__main__":
    import json

    print("=== BƯỚC 1: assess_user_profile ===")
    demo_profile = {
        "education": "Cử nhân Công nghệ Thông tin",
        "skills": ["Python", "Excel"],
        "interests": ["dữ liệu", "công nghệ", "logic"],
        "personality": "Tỉ mỉ, thích làm việc với số liệu",
        "goals": "Trở thành chuyên gia phân tích dữ liệu trong 1 năm tới",
    }
    profile_result = assess_user_profile(demo_profile)
    print(json.dumps(profile_result, ensure_ascii=False, indent=2))

    print("\n=== BƯỚC 2: search_careers ===")
    careers = search_careers(
        interests=profile_result["normalized_interests"],
        skills=profile_result["normalized_skills"],
    )
    print(json.dumps(careers, ensure_ascii=False, indent=2))

    top_career = careers[0]["career_name"]

    print(f"\n=== BƯỚC 3: get_career_details('{top_career}') ===")
    details = get_career_details(top_career)
    print(json.dumps(details, ensure_ascii=False, indent=2))

    print(f"\n=== BƯỚC 4: analyze_skill_gap ===")
    gap = analyze_skill_gap(
        user_skills=profile_result["normalized_skills"],
        target_career=top_career,
    )
    print(json.dumps(gap, ensure_ascii=False, indent=2))

    print("\n=== BƯỚC 5: recommend_learning_path ===")
    plan = recommend_learning_path(
        missing_skills=gap["missing_skills"],
        duration_months=6,
    )
    print(json.dumps(plan, ensure_ascii=False, indent=2))