/* 구성원 데이터
   그룹 순서대로 페이지에 표시됩니다. 사진은 assets/photos/ 에 넣고 photo에 파일 경로를 적으면 됩니다.
   (photo가 비어 있으면 기본 실루엣이 표시됩니다.)
   - about: 관심 분야나 한 줄 소개 (없으면 "" )
   - links: { "이메일": "mailto:...", "홈페이지": "https://..." } (없으면 {} )
   새 그룹(예: "참여 교수", "대학원생")이 필요하면 아래와 같은 형식으로 추가하면 됩니다. */
window.SAIL_MEMBERS = [
  {
    group: "연구소장",
    members: [
      {
        name: "오경석", en: "Oh Kyungseok", role: "연구소장 · 경찰행정학과 교수", photo: "",
        about: "AI를 활용한 공공안전과 조직 위험관리를 연구합니다. 데이터에서 위험 신호를 미리 읽어내고, 사회가 안전하게 대응하도록 돕는 일에 연구소의 역량을 모으고 있습니다.",
        links: {},
        feature: true
      }
    ]
  },
  {
    group: "학부 연구생",
    members: [
      { name: "조원진", role: "학부 연구생", about: "", links: {} },
      { name: "박병준", role: "학부 연구생", about: "", links: {} },
      { name: "강현지", role: "학부 연구생", about: "", links: {} },
      { name: "박가현", role: "학부 연구생", about: "", links: {} },
      { name: "나혜윤", role: "학부 연구생", about: "", links: {} }
    ]
  }
];
