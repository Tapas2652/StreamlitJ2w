"""
JTW Daily Competency Onboarding Dashboard
Joulestowatts Business Solutions Pvt. Ltd.
Founder's Office – Talent Intelligence

Run with:
    pip install streamlit
    streamlit run jtw_dashboard.py
"""

import streamlit as st
from datetime import date

# ─────────────────────────────────────────────
#  PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="JTW Daily Onboarding Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────
#  GLOBAL CSS  (dark theme + brand colours)
# ─────────────────────────────────────────────
st.markdown("""
<style>
/* ---------- base ---------- */
html, body, [data-testid="stAppViewContainer"] {
    background: #0e1117;
    color: #fafafa;
    font-family: 'Inter', 'Segoe UI', sans-serif;
}
[data-testid="stSidebar"] {
    background: #161b22 !important;
    border-right: 1px solid #21262d;
}
[data-testid="stSidebar"] * { color: #c9d1d9 !important; }
[data-testid="stSidebarNavItems"] { display: none; }

/* ---------- hide streamlit chrome ---------- */
#MainMenu, footer, header { visibility: hidden; }
[data-testid="stDecoration"]   { display: none; }

/* ---------- metric cards ---------- */
[data-testid="stMetric"] {
    background: #161b22;
    border: 1px solid #21262d;
    border-radius: 10px;
    padding: 16px 18px !important;
}
[data-testid="stMetricLabel"] { color: #8b949e !important; font-size: 11px; text-transform: uppercase; letter-spacing: .6px; }
[data-testid="stMetricValue"] { color: #f0f6fc !important; font-size: 28px !important; font-weight: 800 !important; }
[data-testid="stMetricDelta"] > div { font-size: 12px !important; }

/* ---------- dataframe / table ---------- */
[data-testid="stDataFrame"] { border-radius: 10px; overflow: hidden; }
.stDataFrame thead tr th {
    background: #21262d !important;
    color: #8b949e !important;
    font-size: 11px !important;
    text-transform: uppercase;
    letter-spacing: .8px;
}
.stDataFrame tbody tr td { color: #c9d1d9 !important; }
.stDataFrame tbody tr:nth-child(even) td { background: #1c2128 !important; }

/* ---------- section headers ---------- */
.sec-hdr {
    font-size: 12px; font-weight: 700; color: #8b949e;
    text-transform: uppercase; letter-spacing: 1.2px;
    border-bottom: 1px solid #21262d; padding-bottom: 9px;
    margin-bottom: 14px; margin-top: 6px;
}

/* ---------- congrats banner ---------- */
.congrats {
    background: linear-gradient(90deg,#1a2d1a,#16201e);
    border: 1px solid #2ea04333; border-left: 4px solid #3fb950;
    border-radius: 10px; padding: 14px 18px;
    display: flex; align-items: center; gap: 14px;
    margin-bottom: 20px;
}
.congrats h2 { font-size: 14px; font-weight: 700; color: #3fb950; margin: 0; }
.congrats p  { font-size: 12px; color: #6e7681; margin: 3px 0 0; }
.congrats strong { color: #c9d1d9; }

/* ---------- total headcount bar ---------- */
.hc-bar {
    background: linear-gradient(90deg,#161b22,#1a1f2d);
    border: 1px solid #1f6feb26; border-left: 4px solid #e63946;
    border-radius: 10px; padding: 16px 22px;
    display: flex; align-items: center; justify-content: space-between;
    margin-bottom: 22px;
}
.hc-label { font-size: 11px; color: #8b949e; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 4px; }
.hc-num   { font-size: 26px; font-weight: 900; color: #f0f6fc; }
.hc-num span { font-size: 13px; font-weight: 400; color: #6e7681; }
.hc-today { font-size: 14px; font-weight: 700; color: #58a6ff; }
.hc-mtd   { font-size: 17px; font-weight: 800; color: #3fb950; }

/* ---------- POD card ---------- */
.pod-card {
    background: #161b22;
    border: 1px solid #21262d;
    border-radius: 10px;
    padding: 0;
    overflow: hidden;
    height: 100%;
    transition: border-color .2s;
}
.pod-card:hover { border-color: #30363d; }
.pod-hdr  { padding: 9px 13px; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: .8px; border-bottom: 1px solid #21262d44; }
.pod-body { padding: 11px 13px 13px; }
.pod-count{ font-size: 22px; font-weight: 800; color: #f0f6fc; }
.pod-new  { display: inline-block; font-size: 10px; background: #1a2d1a; color: #3fb950; border: 1px solid #2ea04333; border-radius: 5px; padding: 1px 6px; font-weight: 700; margin-left: 6px; vertical-align: middle; }
.pod-up   { color: #3fb950; }
.pod-skills { font-size: 11px; color: #6e7681; margin-top: 5px; line-height: 1.6; }

/* ---------- POD colour accents ---------- */
.p-java       { border-top: 2px solid #f97316; } .p-java .pod-hdr       { color:#f97316; background:#1f1a16; }
.p-frontend   { border-top: 2px solid #a855f7; } .p-frontend .pod-hdr   { color:#a855f7; background:#1d1a22; }
.p-python     { border-top: 2px solid #8b5cf6; } .p-python .pod-hdr     { color:#8b5cf6; background:#1c1a22; }
.p-analytics  { border-top: 2px solid #3b82f6; } .p-analytics .pod-hdr  { color:#3b82f6; background:#16192a; }
.p-dataeng    { border-top: 2px solid #06b6d4; } .p-dataeng .pod-hdr    { color:#06b6d4; background:#161e22; }
.p-security   { border-top: 2px solid #f59e0b; } .p-security .pod-hdr   { color:#f59e0b; background:#1f1c14; }
.p-automation { border-top: 2px solid #22c55e; } .p-automation .pod-hdr { color:#22c55e; background:#161e18; }
.p-devops     { border-top: 2px solid #10b981; } .p-devops .pod-hdr     { color:#10b981; background:#16201e; }
.p-biz        { border-top: 2px solid #fb923c; } .p-biz .pod-hdr        { color:#fb923c; background:#1f1c18; }
.p-salesforce { border-top: 2px solid #6366f1; } .p-salesforce .pod-hdr { color:#6366f1; background:#18192a; }
.p-sap        { border-top: 2px solid #14b8a6; } .p-sap .pod-hdr        { color:#14b8a6; background:#16201e; }
.p-database   { border-top: 2px solid #64748b; } .p-database .pod-hdr   { color:#94a3b8; background:#1a1c20; }
.p-infra      { border-top: 2px solid #ef4444; } .p-infra .pod-hdr      { color:#ef4444; background:#1f1616; }
.p-appsupport { border-top: 2px solid #a78bfa; } .p-appsupport .pod-hdr { color:#a78bfa; background:#1c1a22; }
.p-embedded   { border-top: 2px solid #eab308; } .p-embedded .pod-hdr   { color:#eab308; background:#1e1c14; }
.p-product    { border-top: 2px solid #22d3ee; } .p-product .pod-hdr    { color:#22d3ee; background:#161f22; }
.p-ites       { border-top: 2px solid #f59e0b; } .p-ites .pod-hdr       { color:#f59e0b; background:#1f1c14; }
.p-svc        { border-top: 2px solid #34d399; } .p-svc .pod-hdr        { color:#34d399; background:#16201e; }

/* ---------- footer note ---------- */
.fnote {
    background: #161b22; border: 1px solid #21262d; border-radius: 8px;
    padding: 11px 16px; font-size: 12px; color: #6e7681; margin-top: 8px;
}
.fnote strong { color: #8b949e; }
.fnote b      { color: #c9d1d9; }

/* ---------- sidebar mini card ---------- */
.s-mini {
    background: #21262d; border-radius: 8px; padding: 10px 12px;
    margin-bottom: 8px;
}
.s-mini .lbl { font-size: 10px; color: #6e7681 !important; text-transform: uppercase; letter-spacing: .8px; }
.s-mini .val { font-size: 18px; font-weight: 800; margin-top: 2px; }
.s-mini.green .val { color: #3fb950 !important; }
.s-mini.blue  .val { color: #58a6ff !important; }
.s-mini.red   .val { color: #f0f6fc !important; }

.s-row {
    display: flex; justify-content: space-between;
    padding: 6px 0; border-bottom: 1px solid #21262d;
    font-size: 12px;
}
.s-row:last-child { border-bottom: none; }
.s-row .sl { color: #6e7681 !important; }
.s-row .sv { font-weight: 600; }
.s-row .sv.green { color: #3fb950 !important; }
.s-row .sv.blue  { color: #58a6ff !important; }

/* ---------- live dot ---------- */
.live-dot {
    display: inline-block; width: 8px; height: 8px;
    background: #3fb950; border-radius: 50%; margin-right: 5px;
    vertical-align: middle;
    animation: pulse-live 1.5s ease-in-out infinite;
}
@keyframes pulse-live {
    0%,100% { box-shadow: 0 0 0 0 rgba(63,185,80,.6); }
    50%      { box-shadow: 0 0 0 6px rgba(63,185,80,0); }
}
.tagline { color: #e63946; font-weight: 600; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  DATA
# ─────────────────────────────────────────────
REPORT_DATE   = "Monday, 02 March 2026"
REFRESH_TIME  = "11:00 AM IST"
TODAY_JOINERS = 5
TOTAL_HC      = 3168
MTD           = 23
ACTIVE_PODS   = 18

JOINERS = [
    {"#": 1, "Candidate Name": "Ravi Kumar",   "Client": "DTICI",               "POD": "Java Ecosystem",             "Skill / Role": "Spring Boot Developer",   "Date of Joining": "02 Mar 2026"},
    {"#": 2, "Candidate Name": "Sneha Patel",  "Client": "Deloitte Consulting",  "POD": "Data Analytics & BI",        "Skill / Role": "Power BI Analyst",        "Date of Joining": "02 Mar 2026"},
    {"#": 3, "Candidate Name": "Arjun Mehta",  "Client": "BSH",                 "POD": "DevOps & Cloud",             "Skill / Role": "AWS / Terraform Engineer", "Date of Joining": "02 Mar 2026"},
    {"#": 4, "Candidate Name": "Divya Sharma", "Client": "Coupang",             "POD": "SAP Functional & Technical", "Skill / Role": "SAP HANA Consultant",     "Date of Joining": "02 Mar 2026"},
    {"#": 5, "Candidate Name": "Kiran Nair",   "Client": "Flipkart",            "POD": "Frontend Development",       "Skill / Role": "React.js Developer",      "Date of Joining": "02 Mar 2026"},
]

# (cls, emoji, name, headcount, joined_today, skills)
PODS = [
    ("p-java",       "☕",  "Java Ecosystem",                  87,   True,  "Java · Core Java · Java Backend · Spring Boot"),
    ("p-frontend",   "🎨",  "Frontend Development",            94,   True,  "React.js · Angular · JavaScript · HTML5 · Node.js · UX Design"),
    ("p-python",     "🐍",  "Python & Scripting",              62,   False, "Python · Data Modelling"),
    ("p-analytics",  "📊",  "Data Analytics & BI",             78,   True,  "Data Analyst · Tableau · Power BI · Crystal Report · HR Analytics · Financial Analysis · FP&A"),
    ("p-dataeng",    "🔧",  "Data Engineering & Big Data",     55,   False, "Data Engineer · Big Data · Snowflake · ETL · MDM · Reference Data"),
    ("p-security",   "🔒",  "Security & Compliance",           48,   False, "Cyber Security · Information Security · Application Security · Internal Audit"),
    ("p-automation", "🤖",  "Automation & Testing",            73,   False, "Selenium · Automation Testing · API Testing · ETL Testing · SDET · QA · Performance Engineering · RPA · Automation Anywhere · V&V"),
    ("p-devops",     "☁️",  "DevOps & Cloud",                  91,   True,  "DevOps · Azure · AWS · Terraform · GitHub · Linux · SRE · VMware · VDI"),
    ("p-biz",        "💼",  "Business & Functional Roles",     66,   False, "Business Analyst · Accounts Payable · Recruitment · Talent Acquisition · Sales · Marketing · Pricing · Sourcing · Life Insurance · Invoices"),
    ("p-salesforce", "🌩️",  "Salesforce & CRM",                44,   False, "Salesforce · Salesforce Developer · Salesforce Testing · Microsoft Dynamics CRM · AEM"),
    ("p-sap",        "🏭",  "SAP Functional & Technical",     112,   True,  "SAP · SAP ABAP · SAP ABAP HANA · SAP HANA · SAP FI · SAP GRC · SAP Basis · SAP MDG · SAP PLM · SAP Ariba · SAP PI · SAP QM · SAP TM · SAP Security · SAP BW · SAP BODS"),
    ("p-database",   "🗄️",  "Database & Backend Systems",      69,   False, "SQL · PL/SQL · Oracle · Oracle Cloud · Finacle · AS400 · WTX"),
    ("p-infra",      "🌐",  "Infrastructure & Networking",     57,   False, "Networking · Network Engineer · Network Security · Cisco · Routing · IT Infrastructure · Desktop Support · Technical Support"),
    ("p-appsupport", "🛠️",  "Application / Production Support",83,   False, "Application Support · Production Support · Product Support · Monitoring · ServiceNow · Service Desk Management · IT Asset Management · MFT · Middleware"),
    ("p-embedded",   "⚙️",  "Embedded & Core Engineering",     41,   False, "Embedded C · C++ · COBOL · Firmware · Power Electronics · Mechanical Engineering · AutoCAD Architecture"),
    ("p-product",    "📦",  "Product & Delivery Management",   48,   False, "Product Owner · Product Management · Program Manager · Scrum Master · SDM · SME · Consulting · Project Management · Agile"),
    ("p-ites",       "🖥️",  "ITES",                         1750,   False, "Information Technology Enabled Services"),
    ("p-svc",        "🤝",  "Services",                       310,   False, "Managed Services · Professional Services · Consulting Services"),
]


# ─────────────────────────────────────────────
#  HELPERS
# ─────────────────────────────────────────────
def pod_card_html(cls, emoji, name, count, joined, skills):
    badge = '<span class="pod-up">▲</span> <span class="pod-new">+1 Today</span>' if joined else "···"
    return f"""
    <div class="pod-card {cls}">
      <div class="pod-hdr">{emoji} {name}</div>
      <div class="pod-body">
        <div class="pod-count">{count:,} {badge}</div>
        <div class="pod-skills">{skills}</div>
      </div>
    </div>"""


# ─────────────────────────────────────────────
#  SIDEBAR
# ─────────────────────────────────────────────
with st.sidebar:
    try:
        st.image("1772376231110_image.png", width=160)
    except Exception:
        st.markdown("### 🏢 Joulestowatts")
    st.markdown('<div style="color:#e63946;font-size:10px;letter-spacing:1.5px;text-transform:uppercase;font-weight:600;margin-top:4px;text-align:center;">Time Matters</div>', unsafe_allow_html=True)
    st.markdown("<hr style='border-color:#21262d;margin:14px 0;'>", unsafe_allow_html=True)

    # Profile
    st.markdown("**REPORT BY**", help="Talent Intelligence · Founder's Office")
    st.markdown("""
    <div style='background:#21262d;border-radius:10px;padding:12px 14px;margin-bottom:12px;'>
      <div style='font-size:28px;'>👤</div>
      <div style='font-size:13px;font-weight:700;color:#f0f6fc;margin-top:6px;'>Talent Intelligence</div>
      <div style='font-size:11px;color:#8b949e;'>Founder's Office</div>
      <span style='display:inline-block;margin-top:8px;background:#1f3a5f;color:#58a6ff;border:1px solid #1f6feb44;border-radius:5px;padding:2px 8px;font-size:10px;font-weight:600;'>HR Analytics</span>
    </div>""", unsafe_allow_html=True)

    # Report Info
    st.markdown("**REPORT INFO**")
    st.markdown(f"""
    <div style='margin-bottom:12px;'>
      <div class='s-row'><span class='sl'>Date</span><span class='sv'>02 Mar 2026</span></div>
      <div class='s-row'><span class='sl'>Day</span><span class='sv'>Monday</span></div>
      <div class='s-row'><span class='sl'>Refresh</span><span class='sv'>{REFRESH_TIME}</span></div>
      <div class='s-row'><span class='sl'>Joiners Today</span><span class='sv green'>+{TODAY_JOINERS} ▲</span></div>
      <div class='s-row'><span class='sl'>MTD</span><span class='sv green'>+{MTD} ▲</span></div>
      <div class='s-row'><span class='sl'>Total PODs</span><span class='sv blue'>{ACTIVE_PODS}</span></div>
    </div>""", unsafe_allow_html=True)

    # Mini headcount cards
    st.markdown("**HEADCOUNT**")
    st.markdown(f"""
    <div class='s-mini red'><div class='lbl'>Total Workforce</div><div class='val'>{TOTAL_HC:,}</div></div>
    <div class='s-mini green'><div class='lbl'>Today's Joiners</div><div class='val'>+{TODAY_JOINERS} ▲</div></div>
    <div class='s-mini blue'><div class='lbl'>MTD Onboardings</div><div class='val'>+{MTD}</div></div>
    """, unsafe_allow_html=True)

    st.markdown("<hr style='border-color:#21262d;margin:14px 0;'>", unsafe_allow_html=True)
    st.markdown('<div style="font-size:11px;color:#6e7681;"><span class="live-dot"></span> Live · Auto-refreshed</div>', unsafe_allow_html=True)
    st.markdown('<div style="font-size:11px;color:#6e7681;margin-top:10px;"><strong style="color:#c9d1d9;">Joulestowatts Business Solutions Pvt. Ltd.</strong><br>Founder\'s Office</div>', unsafe_allow_html=True)


# ─────────────────────────────────────────────
#  TOPBAR
# ─────────────────────────────────────────────
tcol1, tcol2 = st.columns([3, 1])
with tcol1:
    st.markdown(f"### 📊 Daily Competency <span style='color:#58a6ff;'>Onboarding Dashboard</span>", unsafe_allow_html=True)
with tcol2:
    st.markdown(f"""
    <div style='text-align:right;padding-top:8px;'>
      <span style='background:#21262d;border:1px solid #30363d;color:#8b949e;border-radius:6px;padding:4px 12px;font-size:12px;'>📅 {REPORT_DATE}</span>&nbsp;
      <span style='background:#1f2d1f;border:1px solid #2ea04326;color:#3fb950;border-radius:6px;padding:4px 11px;font-size:12px;font-weight:600;'><span class="live-dot"></span>Live</span>
    </div>""", unsafe_allow_html=True)

st.markdown("<hr style='border-color:#21262d;margin:6px 0 18px;'>", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  CONGRATS BANNER
# ─────────────────────────────────────────────
st.markdown(f"""
<div class="congrats">
  <span style="font-size:28px;flex-shrink:0;">🎉</span>
  <div>
    <h2>Congratulations! New Talent Successfully Onboarded Today</h2>
    <p>We welcome <strong>{TODAY_JOINERS} new team members</strong> to the Joulestowatts family today. Our workforce is growing strong!</p>
  </div>
</div>""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  KPI METRICS
# ─────────────────────────────────────────────
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.metric("Today's Joiners",  f"{TODAY_JOINERS}", f"+{TODAY_JOINERS} new today")
with c2:
    st.metric("Total Headcount",  f"{TOTAL_HC:,}", "All active PODs")
with c3:
    st.metric("Active PODs",      f"{ACTIVE_PODS}", "Competency groups")
with c4:
    st.metric("MTD Onboardings",  f"+{MTD}", f"+{MTD} this month")

st.markdown("<br>", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  TOTAL HEADCOUNT BAR
# ─────────────────────────────────────────────
st.markdown(f"""
<div class="hc-bar">
  <div>
    <div class="hc-label">🏢 Joulestowatts — Total Workforce (Live)
      <span style="display:inline-block;width:8px;height:8px;background:#e63946;border-radius:50%;margin-left:4px;vertical-align:middle;"></span>
    </div>
    <div class="hc-num">{TOTAL_HC:,} <span>&amp; counting ···</span></div>
  </div>
  <div style="text-align:right;">
    <div class="hc-today">▲ +{TODAY_JOINERS} Today</div>
    <div class="hc-mtd">▲ +{MTD} This Month (Mar 2026)</div>
  </div>
</div>""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  TODAY'S JOINERS TABLE
# ─────────────────────────────────────────────
st.markdown('<div class="sec-hdr">👤 Today\'s New Joiners</div>', unsafe_allow_html=True)

# Build HTML table
rows_html = ""
for j in JOINERS:
    rows_html += f"""
    <tr>
      <td>{j['#']}</td>
      <td><strong style="color:#f0f6fc;">{j['Candidate Name']}</strong></td>
      <td><span style="background:#1f3a5f;color:#58a6ff;border:1px solid #1f6feb44;border-radius:5px;padding:2px 8px;font-size:11px;font-weight:600;">{j['Client']}</span></td>
      <td style="color:#c9d1d9;">{j['POD']}</td>
      <td style="color:#c9d1d9;">{j['Skill / Role']}</td>
      <td style="color:#8b949e;">{j['Date of Joining']}</td>
      <td><span style="background:#1a2d1a;color:#3fb950;border:1px solid #2ea04344;border-radius:6px;padding:3px 9px;font-size:11px;font-weight:700;">✅ Joined</span></td>
    </tr>"""

st.markdown(f"""
<div style="background:#161b22;border:1px solid #21262d;border-radius:10px;overflow-x:auto;margin-bottom:22px;">
<table style="width:100%;border-collapse:collapse;font-size:13px;">
  <thead>
    <tr style="background:#21262d;">
      <th style="padding:10px 14px;text-align:left;font-size:11px;font-weight:600;color:#8b949e;text-transform:uppercase;letter-spacing:.8px;">#</th>
      <th style="padding:10px 14px;text-align:left;font-size:11px;font-weight:600;color:#8b949e;text-transform:uppercase;letter-spacing:.8px;">Candidate Name</th>
      <th style="padding:10px 14px;text-align:left;font-size:11px;font-weight:600;color:#8b949e;text-transform:uppercase;letter-spacing:.8px;">Client</th>
      <th style="padding:10px 14px;text-align:left;font-size:11px;font-weight:600;color:#8b949e;text-transform:uppercase;letter-spacing:.8px;">POD</th>
      <th style="padding:10px 14px;text-align:left;font-size:11px;font-weight:600;color:#8b949e;text-transform:uppercase;letter-spacing:.8px;">Skill / Role</th>
      <th style="padding:10px 14px;text-align:left;font-size:11px;font-weight:600;color:#8b949e;text-transform:uppercase;letter-spacing:.8px;">Date of Joining</th>
      <th style="padding:10px 14px;text-align:left;font-size:11px;font-weight:600;color:#8b949e;text-transform:uppercase;letter-spacing:.8px;">Status</th>
    </tr>
  </thead>
  <tbody>
    {rows_html}
  </tbody>
</table>
</div>""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  POD GRID  (3 columns)
# ─────────────────────────────────────────────
st.markdown('<div class="sec-hdr">🗂️ POD-Wise Updated Headcount</div>', unsafe_allow_html=True)

cols_per_row = 3
for i in range(0, len(PODS), cols_per_row):
    row_pods = PODS[i : i + cols_per_row]
    cols = st.columns(cols_per_row)
    for col, (cls, emoji, name, count, joined, skills) in zip(cols, row_pods):
        with col:
            st.markdown(pod_card_html(cls, emoji, name, count, joined, skills), unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  FOOTER NOTE
# ─────────────────────────────────────────────
st.markdown(f"""
<div class="fnote">
  <strong>📌 Note:</strong> This dashboard tracks <b>onboardings only</b>.
  Headcount reflects cumulative active joiners per POD.
  Data is refreshed daily at <b>{REFRESH_TIME}</b>.
</div>""", unsafe_allow_html=True)

st.markdown("<hr style='border-color:#21262d;margin:18px 0 10px;'>", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  FOOTER
# ─────────────────────────────────────────────
st.markdown("""
<div style="font-size:11px;color:#6e7681;display:flex;justify-content:space-between;flex-wrap:wrap;gap:8px;">
  <div><strong style="color:#c9d1d9;">Joulestowatts Business Solutions Pvt. Ltd.</strong> &nbsp;·&nbsp;
    <span class="tagline">Founder's Office</span></div>
  <div><span class="tagline">Time Matters</span> &nbsp;|&nbsp;
    📧 talent@joulestowatts.com &nbsp;|&nbsp;
    <span style="color:#30363d;">Auto-generated · Do not reply</span></div>
</div>""", unsafe_allow_html=True)
