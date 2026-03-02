"""
JTW Daily Competency Onboarding Dashboard
Joulestowatts Business Solutions Pvt. Ltd. – Founder's Office
Run: pip install streamlit && streamlit run jtw_dashboard.py
"""

import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime

st.set_page_config(
    page_title="JTW Daily Onboarding Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

LOGO_B64 = "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"

JOINERS = [
    {"num":1,"name":"Ravi Kumar",   "client":"DTICI",              "pod":"Java Ecosystem",            "role":"Spring Boot Developer",    "doj":"02 Mar 2026"},
    {"num":2,"name":"Sneha Patel",  "client":"Deloitte Consulting", "pod":"Data Analytics & BI",       "role":"Power BI Analyst",         "doj":"02 Mar 2026"},
    {"num":3,"name":"Arjun Mehta",  "client":"BSH",                "pod":"DevOps & Cloud",            "role":"AWS / Terraform Engineer",  "doj":"02 Mar 2026"},
    {"num":4,"name":"Divya Sharma", "client":"Coupang",            "pod":"SAP Functional & Technical","role":"SAP HANA Consultant",       "doj":"02 Mar 2026"},
    {"num":5,"name":"Kiran Nair",   "client":"Flipkart",           "pod":"Frontend Development",      "role":"React.js Developer",        "doj":"02 Mar 2026"},
]

PODS = [
    ("p-java",      "☕","Java Ecosystem",                  "97",  True, "Java · Core Java · Java Backend · Spring Boot"),
    ("p-frontend",  "🎨","Frontend Development",            "106",  True, "React.js · Angular · JavaScript · HTML5 · Node.js · UX Design"),
    ("p-python",    "🐍","Python & Scripting",              "62",  False,"Python · Data Modelling"),
    ("p-analytics", "📊","Data Analytics & BI",             "78",  True, "Data Analyst · Tableau · Power BI · Crystal Report · HR Analytics · Financial Analysis · FP&A"),
    ("p-dataeng",   "🔧","Data Engineering & Big Data",     "55",  False,"Data Engineer · Big Data · Snowflake · ETL · MDM · Reference Data"),
    ("p-security",  "🔒","Security & Compliance",           "48",  False,"Cyber Security · Information Security · Application Security · Internal Audit"),
    ("p-automation","🤖","Automation & Testing",            "73",  False,"Selenium · Automation Testing · API Testing · ETL Testing · SDET · QA · RPA · Automation Anywhere · V&V"),
    ("p-devops",    "☁️","DevOps & Cloud",                  "99",  True, "DevOps · Azure · AWS · Terraform · GitHub · Linux · SRE · VMware · VDI"),
    ("p-biz",       "💼","Business & Functional Roles",     "66",  False,"Business Analyst · Accounts Payable · Recruitment · Talent Acquisition · Sales · Marketing · Pricing · Sourcing"),
    ("p-salesforce","🌩️","Salesforce & CRM",                "44",  False,"Salesforce · Salesforce Developer · Salesforce Testing · Microsoft Dynamics CRM · AEM"),
    ("p-sap",       "🏭","SAP Functional & Technical",      "132", True, "SAP · SAP ABAP · SAP ABAP HANA · SAP HANA · SAP FI · SAP GRC · SAP Basis · SAP MDG · SAP PLM · SAP Ariba · SAP PI · SAP QM · SAP TM · SAP Security · SAP BW · SAP BODS"),
    ("p-database",  "🗄️","Database & Backend Systems",      "69",  False,"SQL · PL/SQL · Oracle · Oracle Cloud · Finacle · AS400 · WTX"),
    ("p-infra",     "🌐","Infrastructure & Networking",     "57",  False,"Networking · Network Engineer · Network Security · Cisco · Routing · IT Infrastructure · Desktop Support"),
    ("p-appsupport","🛠️","Application / Production Support","87",  False,"Application Support · Production Support · Monitoring · ServiceNow · Service Desk Management · IT Asset Management · MFT · Middleware"),
    ("p-embedded",  "⚙️","Embedded & Core Engineering",     "41",  False,"Embedded C · C++ · COBOL · Firmware · Power Electronics · Mechanical Engineering · AutoCAD Architecture"),
    ("p-product",   "📦","Product & Delivery Management",   "48",  False,"Product Owner · Product Management · Program Manager · Scrum Master · SDM · SME · Consulting · Project Management · Agile"),
    ("p-ites",      "🖥️","ITES",                          "1,850",False,"Information Technology Enabled Services"),
    ("p-svc",       "🤝","Services",                        "340", False,"Managed Services · Professional Services · Consulting Services"),
]

# Location distribution data
LOCATIONS = [
    {"city": "Bangalore",  "count": 1196, "pct": 35.7, "color": "#3b82f6"},
    {"city": "Hyderabad",  "count":  660, "pct": 19.7, "color": "#10b981"},
    {"city": "Mumbai",     "count":  430, "pct": 12.8, "color": "#f97316"},
    {"city": "Noida",      "count":  332, "pct":  9.9, "color": "#a855f7"},
    {"city": "Lucknow",    "count":  200, "pct":  6.0, "color": "#f59e0b"},
    {"city": "Others",     "count":  534, "pct": 15.9, "color": "#64748b"},
]

# Experience distribution data
EXPERIENCE = [
    {"band": "0 – 1 Year",   "count":  300, "pct":  9.0, "color": "#22d3ee"},
    {"band": "1 – 3 Years",  "count":  665, "pct": 19.8, "color": "#3b82f6"},
    {"band": "3 – 5 Years",  "count":  832, "pct": 24.8, "color": "#10b981"},
    {"band": "5 – 7 Years",  "count":  732, "pct": 21.8, "color": "#a855f7"},
    {"band": "7 – 10 Years", "count":  530, "pct": 15.8, "color": "#f97316"},
    {"band": "10 + Years",   "count":  293, "pct":  8.7, "color": "#f59e0b"},
]

def build_dashboard_html():
    today_str = datetime.now().strftime("%A, %d %B %Y")
    joiner_rows = ""
    for j in JOINERS:
        joiner_rows += f"""
        <tr>
          <td>{j["num"]}</td>
          <td><strong style="color:#1e293b;">{j["name"]}</strong></td>
          <td><span class="client-tag">{j["client"]}</span></td>
          <td>{j["pod"]}</td>
          <td>{j["role"]}</td>
          <td style="color:#6b7280;">{j["doj"]}</td>
          <td><span class="badge-joined">&#10003; Joined</span></td>
        </tr>"""

    pod_cards = ""
    for cls, emoji, name, count, joined, skills in PODS:
        if joined:
            indicator = '<span class="pod-up">&#9650;</span> <span class="pod-new">+1 Today</span>'
        else:
            indicator = '<span class="wave-dots pod-wave"><span class="dot">.</span><span class="dot">.</span><span class="dot">.</span></span>'
        pod_cards += f"""
        <div class="pod-card {cls}">
          <div class="pod-hdr">{emoji} {name}</div>
          <div class="pod-body">
            <div class="pod-count">{count} {indicator}</div>
            <div class="pod-skills">{skills}</div>
          </div>
        </div>"""

    # Location table rows
    loc_rows = ""
    for i, loc in enumerate(LOCATIONS):
        bar_w = loc["pct"] / max(l["pct"] for l in LOCATIONS) * 100
        loc_rows += f"""
        <tr>
          <td style="padding:10px 10px;border-bottom:1px solid #e2e8f044;color:#374151;vertical-align:middle;">
            <span style="display:inline-flex;align-items:center;gap:8px;">
              <span style="width:10px;height:10px;border-radius:50%;background:{loc['color']};flex-shrink:0;display:inline-block;"></span>
              <strong style="color:#1e293b;">{loc['city']}</strong>
            </span>
          </td>
          <td style="padding:10px 10px;border-bottom:1px solid #e2e8f044;vertical-align:middle;">
            <div style="display:flex;align-items:center;gap:10px;">
              <div style="flex:1;height:16px;background:#e2e8f0;border-radius:4px;overflow:hidden;">
                <div style="width:{bar_w:.1f}%;height:100%;background:{loc['color']};border-radius:4px;animation:bar-grow .9s ease-out forwards;animation-delay:{i*0.08:.2f}s;"></div>
              </div>
            </div>
          </td>
          <td style="padding:10px 10px;border-bottom:1px solid #e2e8f044;color:#1e293b;font-weight:700;font-size:14px;text-align:right;vertical-align:middle;">{loc['count']:,}</td>
          <td style="padding:10px 10px;border-bottom:1px solid #e2e8f044;text-align:right;vertical-align:middle;">
            <span style="background:#f8fafc;color:{loc['color']};border:1px solid {loc['color']}66;border-radius:5px;padding:3px 7px;font-size:11px;font-weight:700;white-space:nowrap;">{loc['pct']}%</span>
          </td>
        </tr>"""

    # Experience table rows
    exp_rows = ""
    for i, exp in enumerate(EXPERIENCE):
        bar_w = exp["pct"] / max(e["pct"] for e in EXPERIENCE) * 100
        exp_rows += f"""
        <tr>
          <td style="padding:10px 10px;border-bottom:1px solid #e2e8f044;color:#374151;vertical-align:middle;">
            <span style="display:inline-flex;align-items:center;gap:8px;">
              <span style="width:10px;height:10px;border-radius:3px;background:{exp['color']};flex-shrink:0;display:inline-block;"></span>
              <strong style="color:#1e293b;">{exp['band']}</strong>
            </span>
          </td>
          <td style="padding:10px 10px;border-bottom:1px solid #e2e8f044;vertical-align:middle;">
            <div style="display:flex;align-items:center;gap:10px;">
              <div style="flex:1;height:16px;background:#e2e8f0;border-radius:4px;overflow:hidden;">
                <div style="width:{bar_w:.1f}%;height:100%;background:{exp['color']};border-radius:4px;animation:bar-grow .9s ease-out forwards;animation-delay:{i*0.08:.2f}s;"></div>
              </div>
            </div>
          </td>
          <td style="padding:10px 10px;border-bottom:1px solid #e2e8f044;color:#1e293b;font-weight:700;font-size:14px;text-align:right;vertical-align:middle;">{exp['count']:,}</td>
          <td style="padding:10px 10px;border-bottom:1px solid #e2e8f044;text-align:right;vertical-align:middle;">
            <span style="background:#f8fafc;color:{exp['color']};border:1px solid {exp['color']}66;border-radius:5px;padding:3px 7px;font-size:11px;font-weight:700;white-space:nowrap;">{exp['pct']}%</span>
          </td>
        </tr>"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<style>
*{{margin:0;padding:0;box-sizing:border-box;}}
body{{font-family:'Inter','Segoe UI',sans-serif;background:#f0f4f8;color:#1e293b;padding:0 2px 0;overflow-x:hidden;}}

/* ── ANIMATIONS ── */
@keyframes pulse-live{{0%,100%{{box-shadow:0 0 0 0 rgba(63,185,80,.7);}}50%{{box-shadow:0 0 0 7px rgba(63,185,80,0);}}}}
@keyframes pulse-red{{0%,100%{{box-shadow:0 0 0 0 rgba(230,57,70,.7);}}50%{{box-shadow:0 0 0 7px rgba(230,57,70,0);}}}}
@keyframes bounce-up{{0%,100%{{transform:translateY(0);opacity:1;}}40%{{transform:translateY(-5px);opacity:1;}}60%{{transform:translateY(-5px);opacity:.5;}}}}
@keyframes blink-badge{{0%,100%{{opacity:1;}}50%{{opacity:.35;}}}}
@keyframes card-pulse{{0%,100%{{box-shadow:0 0 0 rgba(63,185,80,0);border-color:#2ea04326;}}50%{{box-shadow:0 0 12px rgba(63,185,80,.25);border-color:#3fb95055;}}}}
@keyframes joined-glow{{0%,100%{{box-shadow:0 0 0 rgba(63,185,80,0);transform:scale(1);}}50%{{box-shadow:0 0 8px rgba(63,185,80,.5);transform:scale(1.05);}}}}
@keyframes wave-dot{{0%,100%{{transform:translateY(0);opacity:.25;}}40%{{transform:translateY(-6px);opacity:1;}}60%{{transform:translateY(-6px);opacity:1;}}}}
@keyframes glow-text{{0%,100%{{text-shadow:0 0 0 rgba(63,185,80,0);}}50%{{text-shadow:0 0 14px rgba(63,185,80,.6);}}}}
@keyframes bar-grow{{from{{width:0;}}}}
@keyframes fadeIn{{from{{opacity:0;transform:translateY(8px);}}to{{opacity:1;transform:none;}}}}

/* ── TOPBAR ── */
.topbar{{display:flex;align-items:center;justify-content:space-between;padding:14px 0 12px;border-bottom:1px solid #e2e8f0;margin-bottom:22px;}}
.topbar-title{{font-size:16px;font-weight:700;color:#1e293b;}}
.topbar-title span{{color:#58a6ff;}}
.topbar-right{{display:flex;align-items:center;gap:10px;}}
.date-chip{{background:#e2e8f0;border:1px solid #cbd5e1;color:#475569;border-radius:6px;padding:5px 14px;font-size:12px;font-weight:500;}}
.live-chip{{background:#dcfce7;border:1px solid #86efac;color:#16a34a;border-radius:6px;padding:5px 13px;font-size:12px;font-weight:600;display:inline-flex;align-items:center;gap:7px;}}
.live-dot{{width:9px;height:9px;background:#3fb950;border-radius:50%;flex-shrink:0;animation:pulse-live 1.5s ease-in-out infinite;}}

/* ── CONGRATS ── */
.congrats{{background:linear-gradient(90deg,#f0fdf4,#ecfdf5);border:1px solid #86efac;border-left:4px solid #16a34a;border-radius:10px;padding:16px 20px;display:flex;align-items:center;gap:16px;margin-bottom:28px;animation:fadeIn .5s ease;}}
.congrats h2{{font-size:14px;font-weight:700;color:#15803d;margin:0;}}
.congrats p{{font-size:12px;color:#475569;margin:4px 0 0;}}
.congrats strong{{color:#1e293b;}}

/* ── METRICS ── */
.metrics-row{{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-bottom:28px;}}
.metric{{background:#ffffff;border:1px solid #e2e8f0;border-radius:10px;padding:18px 18px 14px;animation:fadeIn .5s ease;box-shadow:0 1px 4px rgba(0,0,0,0.07);}}
.metric.g{{border-color:#bbf7d0;background:#f0fdf4;animation:card-pulse 2.5s ease-in-out infinite;}}
.metric.b{{border-color:#bfdbfe;background:#eff6ff;}}
.metric-lbl{{font-size:11px;color:#64748b;font-weight:600;text-transform:uppercase;letter-spacing:.6px;margin-bottom:8px;}}
.metric-val{{font-size:30px;font-weight:800;color:#1e293b;line-height:1;}}
.metric.g .metric-val{{color:#3fb950;animation:glow-text 2.5s ease-in-out infinite;}}
.metric.b .metric-val{{color:#58a6ff;}}
.metric-up{{color:#3fb950;display:inline-block;animation:bounce-up 1.2s ease-in-out infinite;font-size:20px;}}
.metric-delta{{font-size:11px;color:#3fb950;font-weight:600;margin-top:6px;}}
.metric-sub{{font-size:10px;color:#94a3b8;margin-top:3px;letter-spacing:.3px;}}

/* ── HC BAR ── */
.hc-bar{{background:linear-gradient(90deg,#eff6ff,#f8fafc);border:1px solid #bfdbfe;border-left:4px solid #c1121f;border-radius:10px;padding:18px 24px;display:flex;align-items:center;justify-content:space-between;margin-bottom:28px;box-shadow:0 1px 4px rgba(0,0,0,0.07);}}
.hc-label{{font-size:11px;color:#64748b;text-transform:uppercase;letter-spacing:1px;margin-bottom:5px;display:flex;align-items:center;gap:7px;}}
.red-dot{{width:8px;height:8px;background:#c1121f;border-radius:50%;animation:pulse-red 1.5s ease-in-out infinite;flex-shrink:0;}}
.hc-num{{font-size:28px;font-weight:900;color:#1e293b;}}
.hc-num .sub{{font-size:13px;font-weight:400;color:#64748b;}}
.hc-today{{font-size:15px;font-weight:700;color:#58a6ff;}}
.hc-mtd{{font-size:17px;font-weight:800;color:#3fb950;animation:glow-text 2.5s ease-in-out infinite;margin-top:4px;}}

/* ── WAVE DOTS ── */
.wave-dots{{display:inline-flex;align-items:flex-end;gap:2px;margin-left:4px;vertical-align:middle;}}
.wave-dots .dot{{display:inline-block;font-size:18px;font-weight:900;line-height:1;animation:wave-dot 1.4s ease-in-out infinite;}}
.wave-dots .dot:nth-child(2){{animation-delay:.2s;}}
.wave-dots .dot:nth-child(3){{animation-delay:.4s;}}
.wave-dots:not(.pod-wave) .dot{{color:#2563eb;}}
.pod-wave .dot{{color:#cbd5e1;font-size:15px;}}

/* ── SEC HEADER ── */
.sec-hdr{{font-size:12px;font-weight:700;color:#475569;text-transform:uppercase;letter-spacing:1.2px;border-bottom:1px solid #e2e8f0;padding-bottom:10px;margin-bottom:16px;margin-top:4px;}}

/* ── JOINER TABLE ── */
.table-wrap{{background:#ffffff;border:1px solid #e2e8f0;border-radius:10px;overflow:hidden;margin-bottom:28px;overflow-x:auto;box-shadow:0 1px 4px rgba(0,0,0,0.07);}}
.jtable{{width:100%;border-collapse:collapse;font-size:13px;}}
.jtable thead tr{{background:#f1f5f9;}}
.jtable th{{padding:11px 14px;text-align:left;font-size:11px;font-weight:600;color:#64748b;text-transform:uppercase;letter-spacing:.8px;white-space:nowrap;}}
.jtable td{{padding:12px 14px;border-bottom:1px solid #e2e8f0;color:#374151;vertical-align:middle;}}
.jtable tr:last-child td{{border-bottom:none;}}
.jtable tr:hover td{{background:#f8fafc;}}
.client-tag{{background:#dbeafe;color:#1d4ed8;border:1px solid #93c5fd;border-radius:5px;padding:2px 8px;font-size:11px;font-weight:600;white-space:nowrap;}}
.badge-joined{{background:#dcfce7;color:#15803d;border:1px solid #86efac;border-radius:6px;padding:3px 9px;font-size:11px;font-weight:700;white-space:nowrap;animation:joined-glow 2s ease-in-out infinite;display:inline-block;}}

/* ── DIST TABLES ── */
.dist-row{{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:28px;}}
.dist-box{{background:#ffffff;border:1px solid #e2e8f0;border-radius:10px;overflow:hidden;box-shadow:0 1px 4px rgba(0,0,0,0.07);}}
.dist-box table{{width:100%;table-layout:fixed;border-collapse:collapse;}}
.dist-thead tr{{background:#f1f5f9;}}
.dist-thead th{{padding:10px 10px;text-align:left;font-size:10px;font-weight:600;color:#64748b;text-transform:uppercase;letter-spacing:.7px;white-space:nowrap;overflow:hidden;}}
.dist-thead th:nth-child(1){{width:28%;}}
.dist-thead th:nth-child(2){{width:34%;}}
.dist-thead th:nth-child(3){{width:18%;text-align:right;}}
.dist-thead th:nth-child(4){{width:20%;text-align:right;}}
.dist-tbody tr:hover td{{background:#f8fafc;}}
.dist-tbody tr:last-child td{{border-bottom:none!important;}}
.dist-total{{display:flex;justify-content:space-between;align-items:center;padding:10px 10px;background:#f8fafc;border-top:1px solid #e2e8f0;font-size:12px;color:#64748b;}}
.dist-total strong{{color:#1e293b;font-size:14px;}}

/* ── POD GRID ── */
.pod-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:13px;margin-bottom:28px;}}
.pod-card{{background:#ffffff;border:1px solid #e2e8f0;border-radius:10px;overflow:hidden;transition:border-color .2s,transform .15s;animation:fadeIn .4s ease;box-shadow:0 1px 4px rgba(0,0,0,0.07);}}
.pod-card:hover{{border-color:#cbd5e1;transform:translateY(-2px);box-shadow:0 4px 12px rgba(0,0,0,0.1);}}
.pod-hdr{{padding:10px 13px;font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.8px;border-bottom:1px solid #e2e8f0;}}
.pod-body{{padding:12px 14px 14px;}}
.pod-count{{font-size:22px;font-weight:800;color:#1e293b;display:flex;align-items:center;gap:8px;}}
.pod-up{{color:#3fb950;font-size:14px;animation:bounce-up 1.2s ease-in-out infinite;}}
.pod-new{{font-size:10px;background:#dcfce7;color:#15803d;border:1px solid #86efac;border-radius:5px;padding:2px 7px;font-weight:700;animation:blink-badge 1.8s ease-in-out infinite;}}
.pod-skills{{font-size:11px;color:#64748b;margin-top:6px;line-height:1.65;}}

/* pod colours */
.p-java{{border-top:2px solid #f97316;}}.p-java .pod-hdr{{color:#c2410c;background:#fff7ed;}}
.p-frontend{{border-top:2px solid #a855f7;}}.p-frontend .pod-hdr{{color:#7e22ce;background:#faf5ff;}}
.p-python{{border-top:2px solid #8b5cf6;}}.p-python .pod-hdr{{color:#6d28d9;background:#f5f3ff;}}
.p-analytics{{border-top:2px solid #3b82f6;}}.p-analytics .pod-hdr{{color:#1d4ed8;background:#eff6ff;}}
.p-dataeng{{border-top:2px solid #06b6d4;}}.p-dataeng .pod-hdr{{color:#0e7490;background:#ecfeff;}}
.p-security{{border-top:2px solid #f59e0b;}}.p-security .pod-hdr{{color:#b45309;background:#fffbeb;}}
.p-automation{{border-top:2px solid #22c55e;}}.p-automation .pod-hdr{{color:#15803d;background:#f0fdf4;}}
.p-devops{{border-top:2px solid #10b981;}}.p-devops .pod-hdr{{color:#047857;background:#ecfdf5;}}
.p-biz{{border-top:2px solid #fb923c;}}.p-biz .pod-hdr{{color:#c2410c;background:#fff7ed;}}
.p-salesforce{{border-top:2px solid #6366f1;}}.p-salesforce .pod-hdr{{color:#4338ca;background:#eef2ff;}}
.p-sap{{border-top:2px solid #14b8a6;}}.p-sap .pod-hdr{{color:#0f766e;background:#f0fdfa;}}
.p-database{{border-top:2px solid #64748b;}}.p-database .pod-hdr{{color:#475569;background:#f8fafc;}}
.p-infra{{border-top:2px solid #ef4444;}}.p-infra .pod-hdr{{color:#b91c1c;background:#fef2f2;}}
.p-appsupport{{border-top:2px solid #a78bfa;}}.p-appsupport .pod-hdr{{color:#7c3aed;background:#f5f3ff;}}
.p-embedded{{border-top:2px solid #eab308;}}.p-embedded .pod-hdr{{color:#a16207;background:#fefce8;}}
.p-product{{border-top:2px solid #22d3ee;}}.p-product .pod-hdr{{color:#0e7490;background:#ecfeff;}}
.p-ites{{border-top:2px solid #f59e0b;}}.p-ites .pod-hdr{{color:#b45309;background:#fffbeb;}}
.p-svc{{border-top:2px solid #34d399;}}.p-svc .pod-hdr{{color:#047857;background:#ecfdf5;}}

/* footer */
.fnote{{background:#f1f5f9;border:1px solid #e2e8f0;border-radius:8px;padding:12px 16px;font-size:12px;color:#475569;margin-bottom:16px;}}
.fnote strong{{color:#374151;}}.fnote b{{color:#1e293b;}}
.dash-footer{{font-size:11px;color:#64748b;display:flex;justify-content:space-between;flex-wrap:wrap;gap:8px;padding:12px 0 2px;border-top:1px solid #e2e8f0;}}
.tagline{{color:#e63946;font-weight:600;}}
</style>
</head>
<body>

<!-- TOP HEADER BAR -->
<div style="display:flex;align-items:center;justify-content:space-between;padding:16px 0 14px;border-bottom:2px solid #e2e8f0;margin-bottom:22px;background:linear-gradient(135deg,#ffffff,#f8fafc);border-radius:12px 12px 0 0;padding:22px 24px 20px;">
  <!-- LEFT: Logo -->
  <div style="display:flex;align-items:center;flex-shrink:0;">
    <img src="data:image/png;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/4gHYSUNDX1BST0ZJTEUAAQEAAAHIAAAAAAQwAABtbnRyUkdCIFhZWiAH4AABAAEAAAAAAABhY3NwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAA9tYAAQAAAADTLQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAlkZXNjAAAA8AAAACRyWFlaAAABFAAAABRnWFlaAAABKAAAABRiWFlaAAABPAAAABR3dHB0AAABUAAAABRyVFJDAAABZAAAAChnVFJDAAABZAAAAChiVFJDAAABZAAAAChjcHJ0AAABjAAAADxtbHVjAAAAAAAAAAEAAAAMZW5VUwAAAAgAAAAcAHMAUgBHAEJYWVogAAAAAAAAb6IAADj1AAADkFhZWiAAAAAAAABimQAAt4UAABjaWFlaIAAAAAAAACSgAAAPhAAAts9YWVogAAAAAAAA9tYAAQAAAADTLXBhcmEAAAAAAAQAAAACZmYAAPKnAAANWQAAE9AAAApbAAAAAAAAAABtbHVjAAAAAAAAAAEAAAAMZW5VUwAAACAAAAAcAEcAbwBvAGcAbABlACAASQBuAGMALgAgADIAMAAxADb/2wBDAAUDBAQEAwUEBAQFBQUGBwwIBwcHBw8LCwkMEQ8SEhEPERETFhwXExQaFRERGCEYGh0dHx8fExciJCIeJBweHx7/2wBDAQUFBQcGBw4ICA4eFBEUHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh7/wAARCADhAOEDASIAAhEBAxEB/8QAHQABAAICAwEBAAAAAAAAAAAAAAYHAQUCBAgDCf/EAE4QAAEDAwIDBQIHDAcFCQAAAAEAAgMEBREGEgchMQgTIkFRFGEjMjdxdYGyFRYYQlWRkpOhsbPTJDRic6LBwiVSVHKCCTNDU2ODtNHS/8QAGwEBAAIDAQEAAAAAAAAAAAAAAAEDAgQFBgf/xAA7EQACAQMBBAgEAggHAAAAAAAAAQIDBBEhBRIxQQYTIjJRYXGBkaGxwTM0FBU1cpLR4fAHI0JDUmKC/9oADAMBAAIRAxEAPwD2WiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAovxM1tbNA6dZfLtS1lTTuqG0+2la0vDnBxB8TgMeH1UoVM9sP5JYvpSH7EiouqkqdGU48UjrbCtKd7tGjb1e7KSTOl+E7of8i6i/Uw/zU/Cd0P+RdRfqYf5qgNPNFpKn0jpyxWvR8IvNljuVddtRRB0VQ+RrnOiLz8VgxtDR6joSSejqnhrZKObVF91LWU1khpHU80FHZS6ohIna/YxpeAQS5oPQNAJxgYA47u7vGkl56cNM8T6NDYHR/fxUpSSfd7Tbl2t3upZWX6+eHoWZ+E7of8AIuov1MP81PwndD/kXUX6mH+aq4ruBsFJpaV8txr23mK2+3ulLYRQl2zf7OPH3m/H423b+5de38KtHuvx0fXajuw1PTW41tW2GlYaTJh7wRMcTuyA5pLiMEehOBDub9PDwvgZR2L0TlFyhvvGc43nouL4cNVr5ln/AITuh/yLqL9TD/NT8J3Q/wCRdRfqYf5qpXX9h0Rb+E2kLvZjcG3W4sne98rBicsk2Sb/ABHbsI2tDRgjmeZVZqirtK6pvDa5P4nVsehOwrym6kKc0k5R1bWsW0/mv7Z774XcQLTxCs1TdLRSV1NDT1Bp3Nqmta4u2tdkbXOGMOClu4Kh+xd8n94+lT/CjVsar05Lfn0xj1HfLOIA8EW2obEJd23m/LTnG3l06ld21qyqUIzerZ8p25YW9ntWrawe7CLwm8vl8SQbgm4LzBojUWqLnxYoLJFqq81Fv+6jwBJVF3ewxOc7xY5Hc1nPl5r06rKNZVU2ka+1tlT2ZOMJyTclnTwOW4JuC4orjk5OW4JuC4ogyctwTcPeuKoXtMXu7R6nstks1zr6Oc0rnubS1L4t7pXhjM7SMn4M4z0z71VWqqlHeOjsrZ8to3KoRlu5y8+GEX5uCbgvjSxdxSxQb3P7tjWbnHJOBjJK+itOe+Ohy3BNwXFEIyctwTcFxRBk5bgm4LiiDJy3BAQVxWW9UGTkiIhIVM9sP5JYvpSH7EiuZUz2w/kli+lIfsSLUvvy8/Q7/RX9s237yK44XN1zBoGxey6r0gKa5yytslvvke+RsrJdjhE4sOHF2MDJGXDoSVCtbv15S6ddJqCsiq5NWXCU1MW3dUioo5O62nADQMuwGsJGBjlyC3dBxHtmm+FuiaagtVkvF7oJK2TdWxOe+3PM4dG9oyBlw59fxR6LaaQ17YYqfQtVerzGLlGL17VVmLvHUNRUygxzubjBzknl6rhN05xUN/kuemuM/V+x9YULu3r1Lr9HTTnP/St57vWOPBZSbjB5ay3qs5RBr1rHW0OnH2W92inaWwC3urq20t9sbDgOEHevbnGMEfjdCD5rYu4ncSbHR0dDWUsVPUGk9mZU1drAqqinxtawyOG5zRyIxzyBklTwazsVmtGlqXVGuYNZ1Ft1N7XUPjbJL3MJgeGEOeMyBj3B+eZBO0fFXSptWUNi1vpu4ap4mxaxoYbhNUd1FSOeKMPjc1k5djIIcQe6AO3GQM4UbrTyqr5LitPXX6GXXwqRcZWUWu1JdmXaaT7vY0zhd7C1WMlVXu+appNJ0mir1Rmno6V5qKWOqohHPE17i4hriA7Y52T7z8yi6uTjzqe03LTFrstLcLbdamKtkqvaIbjU1skMbm42d5MwYDjglgPhLBy55VNrRuY7s91Szg9TsWs69r1sqXVuTba8Xnj78f58T1h2Lvk/vH0qf4UauXU9wbadN3O6vJDaOklnJAyfAwu/yVNdi75P7x9Kn+FGp3x9r/YOFV3LT46kR0zffve0O/w7l6izlu2cX5HwvpDQ/SOktSl/yml8cFN9mOg9p4j+0PYXCioJZA4+TyWsH1kOd+1elbrcaC1UEtfcqyCjpYhl8szw1rfrP7lSvZPoCINQXVw5PfDTMPoWhznfbatVrKtqeJnGmn0n38gslBUuicxhIB7sEzSH+0SCwHy5Y6nMUJ9VRWOLZubZtP1ntiqpSxClFOT8ks6eeWWe3irpWSCSsgivc9uiJElwitFQ6mbjqS8M6DzKllju9svlujuNorYa2lk+LJE7Iz5g+hHmDzC7FJSUtLRR0VNTxQ00UYjjiY0BjWgYDQPTCoDgXWPs3GO/6ao3OFsmmqmNh6taYZSGOHp4cj38vQLYlUlTlFS1ycGjY217b1qlunF01nVp5XPksPn4cvMubVustNaTNMNQXNtEakPMIMT37g3G74jTjG4dfVbynljngjniJMcjQ9pIIyCMjkeYXnjtFufe+Kdl06x3h7iGAe588pB/YGL0S0Na0NAAaBgD0CmnUc5yXJFW0Nn0rWzt6qb36ibfhjljTw8zo2u8W251NfTUFSJpbfP7PVAMcO7kwHbckYPIjpnqqD1dnUPacoqHwllJWUzG+9sTBM4fn3hWXwJ/pWk7hfef+2rzWVzSf90yljf2MVacE/8Ab3HS73snfHH7ZVRu643yBjR+i8/mVFaTqKCfNna2XQjY1bycf9uDj/6f9Uy/b7d7bY7ZLc7vWRUdJFgPlkPIEnAHqSScYCiY4u8PCSBqIHBwcUk5/wBCh/aurxHYbHa8nM9W+oIB6iNm3n9cqk3DnVOibHoGyW2XVVip5YaKMzsdXxAtkLdz88+R3F2Va6z6xwTSwc+lsmktnwupwnOU20lF4wlz7suZLdLalsuqKKWssdYauCGXunv7l7MPwDjxgZ5OH51qr1xE0naro+1SXCWsuDM76agpZKqRmOu4RtO0j0K2Gv57jT6HvdRaBI6vjoZXQd2MvDtpwWjzI6geoVGdnbXWn9ONrLReC2lNfO2aK4O5sPhADHu/FHIkO6eJ2ceapWcJKDfHmRYbJp3dvVuoRlJQaSimt71b3eXlHX2L20vqa2ajjqHW5tcw07mtlZVUUtO5pOccpGjPTyyvtcL/AGmhvNFZqiraLjXf1ena0ue8DOXchyAweZx0WyY5r2Nexwc1wyHA5BHqFTvsOorrx1mdHd7Ya6zW0bZ3W95iZvJwwsEoJdtlPi3D5lsRTxqcGq4ObcE0vBvPzwvoXGi01RfaC0NpKC9XWmdc5IQ4xwxO3ykDxPbE3c4Nzn1x6rv2y4UN0o21luq4aqncSBJE8OGR1Hzj0UlZ2llvVYWW9UJOSIiEhUz2w/kli+lIfsSK5lTPbD+SWL6Uh+xItS+/Lz9Dv9Ff2zbfvIrHRVworlwqZXwaD0VNdmXmlssD6i3EtkEjAN8h3ZLycEuHv5KOao4d6XhtOo2ac1Bca276WIbdGVVK2OGbD+7eYSDkbXZ5O645Z6rrWmx65jtGntH22ej9k1TOy6UMkTyHMlYMZL8ZaWAZIGcLZauvPEi/aU1VS3ie101JZKmGC9yRU7Ypq6YSFjA5zW/CEObnyGMH0Xn24yp4nF5S8PLP8n6H1+FOrQunK2rRUZTTxvcnJRWU085e/FJNdp8fCpEQgg4II8+a3VFpq41ekK/VMToPYKCojp5g557wvf8AFwMYI+tc2MXLge2qVoUknN4y0vd6Je7NKiIoLD1h2Lvk/vH0qf4Ua7vaquscdhtFkbKO+nqjUvYDz2MaWjPuLnjHrtPoo/2V7U698I79bm3S5WsyXYH2m3y93OzayJ2GuwcZxg+oJCmcHC3RlNdPulfqzUV+myCTcxJI12Om4tYC4e5xI9y9VbqUrSMVzXE+EbTnbW/SKvc1pNuMtIpZb7KxrwX9DY9nW0y2vhlSzTxujkuEz6za4c9rsNYfmLWNcPcVXnBOnfbePV8oLiNlUyKsY0O6ucZo3Aj52ZcPcVc9RrPSlCwNqLvT0zWDGHtcwADy5hQTWNz4U6gu9NeY9cUlpvlIR3NfRVDWycsgNcHAhw5kYI6EjoSFfOMUoYa7Jy7S5uK1W5dWlJKsnqot7r5cuHJ8yydVXqj07p6tvVe8NgpIi8jPN7ujWj3uJAHvKpXsy2Ourr9dNa17Tsc18MbyMCWZ7w6Vw9wxj08RHkVsLodDajqYDq3iw69UlO7eyiY6OmiLumXCNoJPPrkEZOCMkKwtO6v0GTR2KxXq1N5CGlpadwaOQ5NaFllVKik2kl5lShUsLCpQpQlKdTvS3ZJKK5LKT9XhIpysfHW9qlorn7Y2XGNrN55Aspx3YHzua363K7eJF7i09oe73WSRrHx0z2wAn40rhtY0fO4hQLiLprhzqzVBll1KLXfe9bTS9w4fCSNO1oc0j4w5NBBHQZzgY2lBw6sthkiv2rNSXe+ttzhLCbnUOkgp3A4Dww55g46nA6+WUjSqwclji+JjdbR2ZewoVZVfwoqLhjju+fBZ8XwWuORtLNFJo3gnEKhjo57bZDLM3HMSiIucPn3Eqv8AsmW8sgv9yc0bSYKZh9C0Oc77TFabrhpfW9quNjprnDXQzQFlQ2B5D2tdyznyWl0bwvtulLhFU2rUWoxC2TvZKR1WwQTO248bWsGfL8wWU6MlUi0tEU2u1berYXMJSxOq08pZTw84088lZdo1zr1xRsmnonkfAQwgjq188paf2BhV2jRuj2kFulLECOhFvi//AColxK0Poyv1HS6gvV8uNnuEzmRwOpp2sL5GY2FoLHEOHLG3Hl5r63TRbbfCH1fETX7GOO0Ojqu8weQ57YjjmRjPVRGlOM5Scc5La+0Lava0KFOs4OmtVh8XryLFVL8feHmn2adrtW2+OO3V0DmvmZGA2Kp3PDTlvQPy7OR1PXOciyr1bo9TUMcdJe71aX08u7vKJ5gl3bfiva9pyMOBwR6FaCq4X0N0ljOpNSakv8Ebg5tLV1TWQ59S2Jrcn3+8rOtBzi44NPY91CyrRr9c44eqSbbXh4a+b0Nb2Zn3KThwfbnyOpxWyNod5ziIBoIH9kP7we7BX14SPFdf9camc0ubPczTx45kshBx+cOap851uslrYMQUNDThkbGtaGsjBIa1oA6DJAUX0xpiLTGoKmhteopY4K+V9wNtkgY8gBzQ8tf1DfE1vP3eYJVlKG5BRNHaF0ru6nXSwpNvH9/M03AFsl0td21hXnvbnda14dIeZbG0DawegBJ5egb6JwrmdPxK166jLvucKxnL8XvsuDiPLJIdk/NnyW/pNHyWeOuo9PX6a00VbI6d0AgZIYHHAcYSfiDpyIcB5YW30jp61aZssdttERbBne+Rztz5nnq9zvMnl+zHJWGkbdZb1WFlvVQSckREJCpnth/JLF9KQ/YkVzKjO23WOoeDtPM1gfm7wNIJx1ZKq6tvO5g6NPvS0R1dh3tGx2hRuazxCEk3z0K54b6ssVFwelrq2509NqPTLa6GyxGUCU+1taA9jTzO15eTgHAUouutNCCv0tV1NdRVFNqG6x3i9wsc14pJGUjI2Rytac4Ex7wgjq13ovIrtSFrg10EQJ6Av6rl98Mn/Cs/SKrj0d2vGKj1ceXNcv6aHuq/SHotWrSrO4mt5y4RfCWuFpyl215nrmm1HTQ3XTH39a10xfrzFqDv6atoZ4nMpKPunB4kka1rWNLi0hp9x8uXT0Jr2w1sOoKzWVytr3OvtO2hjxGGRMYHthk7ppaXxRnaTjyGST5+Uvvhk/4Vn6RXH75Dy+Ai5nHx/P0WS6PbXTTUF/EvDGviVPbvRWcJRdeWXjVU2sYlvdlJdnPh7lnavtdTLJdb1dtTW+53T21zZTTzNmbOS747HtOCCOYAHIemCBE1Hm6ie4bm08ZB8w8odRPBANNGM8h4zzWjPohtSTyoL+JHqLf/ABH2BShuSrN4/wCjWF4JJcD2j2Lvk/vH0qf4UavOZ7425ZDJKfRhaD+0hefewpXvuHDq/PfG1nd3ksABzn4CI/5r0KuhRtalpBUavejxPknSC/o7Q2lVuqDzCTyuXJGsqbnWw/E07dJ/7uSm/wBUoWlr7+XgtrNAahmac5zTU0o/ZKVJ5xU/+A+Ee57T+8FdCpfqJv8AVqe0yf3k0jP3NKtxk42+4aogNyuujsn2/hJeX46ufpyJw/PlaCXUnCi3VsFc7h/dbfUU0rJopG29sJY9pBaeUg8wFZc1Zr2M+Cxafl/5bnKP3whdCovnEeE+HQ9DOMdYrs3/AFAJ1MXyXyJ/W9amsKc8eSl9in+MdP7DxDqqykeAyrZFW072/wBpo5/pNcVftfHFqbRcsbMFlzt5LCP/AFI8tPP5wqj46QV9Za9PaguNtNvrJGSU1VBvD+7cDuYNw5HlvKnfCa9044VUtfXTNiit0csc7yeTWxk4/wAO1bFTLhF+B5+y3YXlam+Eln7/AHKu4BVxo+IMVO8loraaSEj+0AHj7B/OvRa8rUNxfb+IFLenQPo2Or2VgjeObYZHh4+osd19Crz4t3ergtVPpy0Hdd73J7NCBnLIzye846DBxnyyT5JWjmS8yNkXKpW009d1/Xh8WajTLTrjiPU6okIks1lcaa2tIy2SXzkH7/rZ6Ke32nmqoKaniZuBrIZJHZxsbG8SZ+ssDf8AqXX0/bLfpPSsNCx7YqShgL5ZXcs4Bc95+c5KpPW991lHHbNYC81dHDcpJX0VExzmthiYW7Nzc4duBycj9+Bgo9Y9OBtyrqxpb01mT1ePb5LRIte6Wi51j7hUPilkJgrDDTunwx8jtjIMc8DDYt3PoZM8iuNxtVxpaoNoo6iShL4GVDd3eun2xy7pHNLxuy50Qdzy7bzyMqT2upFbbaWtGMTwslGOniaD/mqi4vVV80gyhfQ6wvU01Y+Qlkro9rGNx02sB6uCwhHeeDcubpW9PrGsr2J/drFVVmnKWxiaZ0Uhk9okkIBY0skLG9T8V5jxjPJnXzXT9kvRnZeam1/0yqphHUx5bJ3DXvaTEAHDdsDBkA43Pe4EjIP00TZbqyltl3uOqLzVyyUzJZqSZ0fc7ns5jAaHYBPLn5BRHjBNetK0dPXUGrry6asqnAQPfH3bGYLjtAZnkdoGSeSlQzLdTMKt26VHrZQePb+Zv5LFXS2qsNVa5H1gtVXFRkmMlhmlkd3XJxaC1vdAAHb1AOAu8LdXsuVRJBSVEccBZLb2MYxrWsbE0iEO3+EOfuDgW5O7rgAjr8PrVd6i02i/XHVN5qHz07Z30j3RiF25uQCNu7HMHqtBf9WXLUHElmi7VdXWaijkdFUVUQHfSva0lzWkjw8xtHvBPPkEUMvCEr1QpxnKLW80ktNc+5LrZaKq3Xa2QwxTVMMFM2KqmqDuG4Md8Kx27cZHOIa4Ec2gcxtAdKW9VGLTpAW6409a3U+p6nuSSYam4GSKTljxNI+vlhSdvVYPHI2acpSXaWDkiIoLQqC7d3yKU/0zT/YlV+qgu3eQ3gnTuJwBeYCT/wC3KtzZ35qn6oqr/hyKosp1xaLPw2oOF+l6W66eu9rp5rwRbI6iGurnvc2riq5ixxjazAbzI2jPXbgdOo4M6aqdDXHUs9U+kraiO7VcYttS6ooaB1NK9rIGhsDu8i8JDpDIwtG3AIyVD7Pwy4o0UVRa6a6vs0M7qRs9P90p4opnVOGta4RtLCWuBjcHc9zHNaHnGehatA61fFedN02oqWjpKSrEFwon19RFA9xhMoc6IMwfCwja5veAtILRsdt9LuxTbhUS5tri15/FGk233ofQs626D4aWjXvEHRlNp/U1/qrXpZ8+2V9PLL3h7l7jTAREtlDZYw1+Mj4TkdwxsL8+hsnC7WlVPV3uru9TpfT9KasOpmbKepjexkDQ2EfB7g4SA83s2jcCNxqO6aF4mWTvNTx11ZU3MzMp5HW2ummr9z4BJguYMnDPC4biRtPItG5dqbhVxVnndbpXVM4me2ma11dI6OobDAJo8Z5OY3eI2Z5CR2wYOcYulCTTlVT4fLGfoIyaWFAuHVfBKw3/AFXfbrfNRXqura66VNOatgbvpe5gY5rnxQUxbI5xwS3MQ7vmMkEnRUeiLRo7htryKgodRT1EmjYJ5r1OGfc2t78xyYp8N/FPIeI5w7PQE1e7Sev2zU9LJqh0Z1Ja3XRwkudSxtZCImPxLuaN52OA3OzH4XgvGx2Ni3hzxKdSmxjVMH3PimbRCmN3qBT4f0wwtxsMje7IAzvAJG3D1CptJRlWWNNPR/2sfcZWcqGpfP8A2f8A8m2o/pw//HhXpJebuwAHN4b6ja5pa4Xwgg+R9nhXpFcDan5ufqbdD8OPoERFoFoREQEH45W/2/h3WSNZufRyR1Lfdg7XH9FzlVfC5ldqGH7ymNc21zVYr7jI1xHwTWtHd/8AU4M/N7ivQF7oWXOzVttkIDaqnkhJPluaRn9qivBzSz9NaUY+sh7u5V2JqkEc4xjwx/UOvvJV8Km7TaORdWUqt5Ga7uNfbl75+BXHaKtjKbVFDWRxtZFVUQjw0YGYyQf8Lmj6lMeEtJW3+vk1zeW/CGBtFb2HmGMYAHvH/M7d+d3kVsuL2lJ9VU1mp6UFskddtlk/8uFzSXu/wtx78BTO3UdNb6CnoKOIRU9PG2KJg6NaBgBJVP8ALS5ijYtXs6j7uj9Xj7akE41Xqjp7bQ6dqqz2SK6zhtZMASY6VpBkIABOXcmjl5lQ7jTqTS1807bKWw18c0lHUACJkL2BkWwjluaBgYaMKxtK2uun1betUXemfBLI4UVuikxmOlZz3cum93ix7l8eMtlrr7omSlttM+pqo6iKWONhAJwcHGfc4pCUYySMbqjWrUqs1zXDDzhcOfPjw5mw4ZVPtXD6xS5zijZH+gNn+lVbx6e668QbRZIiSe5jiA/tyyEfuDVY/CGhuds0JSW+70klLUwSSt7t+M7S8uB5E/7yh1Xpi/3Pjiy9VVrnjtUVUx7J3Fu3bFGNp655vb6eamDSm2RdxnVs6VNJ5lup+XqW8xrWMDGDDWjAHoFSHaNqXVeorNZofFKyBzw0ebpXhrf4avBVBqnTOoLzxnpLk61z/cmnqKcCoO0N2RgPd55+NuCwotKWWbG1YSqUFTis7zSLao6dlJRw0sfxIY2xt+ZowP3KoeKXDGvqLpU6i044zSSv7+ak3YkEmcl8Z8+fPHXPTPIC3quSSGlmmigdUSMjc5kTSAZCBkNBPIE9Oaik2r70A6ODQGoH1OPC17oWxk+hfvIA9+FFNyTyiy9pUKsNyqn5YT+yIpwZ4gXO6XJum74XVE3duMFU7lIS0ZLH+vIHn15c85yrcb1VbcMND3K23+t1VqEQR3GrdIWUsJDhCZHbnEkcs+QAyAM8znlZLeqVd3e7I2aqyoJVuPnxxyyckRFWdAKDcbuHkPEzRDtOyXWe1yx1DKqnqYmB+2VgcG7mnGW+I9CD05qcos6dSVOSnHiiGk1hn518X+HfFTh/UNqdSVN0rrbT1Amp7tBVyzQMk3Eh+4ndE/LicuAO5xwTnJgtJqjU9J/VNS3qnzIJfgq+VnjDAwO5O+MGANB67QB05L9TJY45onxSsbJG9pa9jhkOB6gjzC8/cW+y5pLUpmuWjpGaYubsuMDGZopT/dj/ALr52ch12kr0dptqnLs14481w+BoVbSXGmzy5RcPNd6h0vSXZ1QyezOjMzX1Nc5zIAO7jy5pyW+EsHIHwsx5AHnebFxNtliq7xVXm6SW2lhp6h80V0lex0U1Q8RPbz5gyM3+o3scQC5fHXemeJ3DKvhor8+92qNm6Gjqqatk9le0ua4tikadoyY2O2cneBpLRgL4aHsnEriHXyWnTkl+uwJeKlz6yT2eISHLzK9zto3ElxB5u58nFdbLcd9yju/b1NbTO7h5I+3Umo2ymZuobwJDG6IvFdKHFjg0OZnd8UhjAR0Ia30Cn3C/TPGbiNWh2m7rqH2UTb5LnVXSeKmjk2d2Xd5klz9g2HYHOAwDgL0Jwi7K2nLGIbnryoZqG4gB3sUYLaKI+hBw6bHq7DT5s816JpKenpKaOlpIIqeCJoZHFEwNYxo6AAcgPcuVebZpR7NCKb8XwNijaT4zZXvZ/wCFtPwp0dPZGXWS51FXU+1VM3dCNgfsazaxvMhoDR1JJ68ugsbaFlF5yrVlVm5zeWzoKKisIxtCbQsoqyTG0JtCyiAxtCbQsogMbQm0LKIDG0JtCyiAxtCbQsogMbQm0LKIDG0JtCyiAxtCAALKIAiIgCIiAIiIDrXW30F1t09uulFTV1FUMLJqeoiEkcjT5OaeRHzr5WKz2qw2uG12W3UluoYBiKnpohHG35gOX/2u8ineeMcgERFACIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiID//Z" style="height:64px;object-fit:contain;filter:drop-shadow(0 2px 6px rgba(0,0,0,0.15));border-radius:6px;" />
  </div>
  <!-- CENTER: Company Name + Tagline -->
  <div style="text-align:center;flex:1;padding:0 20px;">
    <div style="font-size:22px;font-weight:900;color:#1e293b;letter-spacing:-0.5px;line-height:1.2;font-family:Georgia,serif;"><span style="color:#00a896;">Joulesto</span><span style="color:#c1121f;">watts</span> Business Solutions</div>
    <div style="font-size:11px;font-weight:800;color:#c1121f;letter-spacing:4px;text-transform:uppercase;margin-top:4px;">TIME MATTERS</div>
    <div style="font-size:11px;color:#64748b;margin-top:2px;font-weight:500;">Daily Competency Onboarding Dashboard</div>
  </div>
  <!-- RIGHT: Date + Live -->
  <div style="display:flex;flex-direction:column;align-items:flex-end;gap:6px;flex-shrink:0;">
    <div style="background:#e2e8f0;border:1px solid #cbd5e1;color:#475569;border-radius:6px;padding:5px 14px;font-size:12px;font-weight:500;">&#128197; {today_str}</div>
    <div style="background:#dcfce7;border:1px solid #86efac;color:#16a34a;border-radius:6px;padding:5px 13px;font-size:12px;font-weight:600;display:inline-flex;align-items:center;gap:7px;"><div style="width:9px;height:9px;background:#16a34a;border-radius:50%;animation:pulse-live 1.5s ease-in-out infinite;flex-shrink:0;"></div>Last refreshed at <span id="refresh-time">11:00 AM</span></div>
  </div>
</div>

<!-- CONGRATS -->
<div class="congrats">
  <span style="font-size:28px;flex-shrink:0;">&#127881;</span>
  <div>
    <h2>Congratulations! New Talent Successfully Onboarded Today</h2>
    <p>We welcome <strong>5 new team members</strong> to the Joulestowatts family today. Our workforce is growing strong!</p>
  </div>
</div>

<!-- METRICS -->
<div class="metrics-row">
  <div class="metric g">
    <div class="metric-lbl">Today's Joiners</div>
    <div class="metric-val">5 <span class="metric-up">&#9650;</span></div>
    <div class="metric-delta">&#9650; New today</div>
  </div>
  <div class="metric b">
    <div class="metric-lbl">Total Headcount</div>
    <div class="metric-val">3,352</div>
    <div class="metric-delta" style="color:#58a6ff;">All active PODs</div>
  </div>
  <div class="metric">
    <div class="metric-lbl">Active PODs</div>
    <div class="metric-val">18</div>
    <div class="metric-delta" style="color:#64748b;">Competency groups</div>
  </div>
  <div class="metric g">
    <div class="metric-lbl">MTD Onboardings</div>
    <div class="metric-val">+23 <span class="metric-up">&#9650;</span></div>
    <div class="metric-delta">&#9650; This month</div>
  </div>
</div>

<!-- FINANCIAL METRICS -->
<div class="metrics-row" style="margin-top:-8px;">
  <div class="metric" style="border-color:#fed7aa;background:linear-gradient(135deg,#fff7ed,#fffbeb);border-top:2px solid #f97316;">
    <div class="metric-lbl" style="color:#c2410c;">Today's OB PO Value</div>
    <div class="metric-val" style="color:#1e293b;font-size:26px;">&#8377;12.5 L</div>
    <div class="metric-delta" style="color:#64748b;font-size:11px;font-weight:500;">Margin: <strong style="color:#22c55e;">&#8377;4.2 L</strong> &nbsp;&#183;&nbsp; Based on 5 joiners</div>
  </div>
  <div class="metric" style="border-color:#e9d5ff;background:linear-gradient(135deg,#faf5ff,#f5f3ff);border-top:2px solid #a855f7;">
    <div class="metric-lbl" style="color:#7e22ce;">MTD OB PO Value</div>
    <div class="metric-val" style="color:#1e293b;font-size:26px;">&#8377;80 L</div>
    <div class="metric-delta" style="color:#64748b;font-size:11px;font-weight:500;">MTD Margin: <strong style="color:#22c55e;">&#8377;27 L</strong> &nbsp;&#183;&nbsp; 23 joiners</div>
  </div>
  <div class="metric" style="border-color:#fde68a;background:linear-gradient(135deg,#fffbeb,#fefce8);border-top:2px solid #f59e0b;">
    <div class="metric-lbl" style="color:#b45309;">Total PO Value</div>
    <div class="metric-val" style="color:#1e293b;font-size:26px;">&#8377;29.72 Cr</div>
    <div class="metric-delta" style="color:#64748b;font-size:11px;font-weight:500;">Total Margin: <strong style="color:#22c55e;">&#8377;7.54 Cr</strong> &nbsp;&#183;&nbsp; 3,352 HC</div>
  </div>
  <div class="metric" style="border-color:#fecaca;background:linear-gradient(135deg,#fef2f2,#fff1f2);border-top:2px solid #e63946;">
    <div class="metric-lbl" style="color:#c1121f;">Pipeline</div>
    <div class="metric-val" style="color:#1e293b;font-size:26px;">16 <span style="font-size:14px;font-weight:500;color:#64748b;">Yet to Join</span></div>
    <div class="metric-delta" style="color:#64748b;font-size:11px;font-weight:500;">PO Value: <strong style="color:#e63946;">&#8377;40.5 L</strong></div>
  </div>
</div>

<!-- HC BAR -->
<div class="hc-bar">
  <div>
    <div class="hc-label">&#127962; Joulestowatts &#8212; Total Workforce (Live)<div class="red-dot"></div></div>
    <div class="hc-num">3,352 <span class="sub">&amp; counting</span>
      <span class="wave-dots"><span class="dot">.</span><span class="dot">.</span><span class="dot">.</span></span>
    </div>
  </div>
  <div style="text-align:right;">
    <div class="hc-today">&#9650; +5 Today</div>
    <div class="hc-mtd">&#9650; +23 This Month (Mar 2026)</div>
  </div>
</div>

<!-- JOINERS TABLE -->
<div class="sec-hdr">&#128100; Today's New Joiners</div>
<div class="table-wrap">
  <table class="jtable">
    <thead><tr>
      <th>#</th><th>Candidate Name</th><th>Client</th>
      <th>POD</th><th>Skill / Role</th><th>Date of Joining</th><th>Status</th>
    </tr></thead>
    <tbody>{joiner_rows}</tbody>
  </table>
</div>

<!-- LOCATION & EXPERIENCE DISTRIBUTION -->
<div class="sec-hdr">&#128205; Location &amp; Experience Distribution</div>
<div class="dist-row">

  <!-- LOCATION TABLE -->
  <div class="dist-box">
    <div style="padding:14px 16px 10px;border-bottom:1px solid #e2e8f0;display:flex;align-items:center;gap:8px;">
      <span style="font-size:16px;">&#128205;</span>
      <span style="font-size:12px;font-weight:700;color:#475569;text-transform:uppercase;letter-spacing:1px;">Top Locations</span>
    </div>
    <table style="width:100%;border-collapse:collapse;">
      <thead class="dist-thead">
        <tr>
          <th>City</th>
          <th>Distribution</th>
          <th>Headcount</th>
          <th>Share</th>
        </tr>
      </thead>
      <tbody class="dist-tbody">
        {loc_rows}
      </tbody>
    </table>
    <div class="dist-total">
      <span>Total Workforce</span>
      <strong>3,352</strong>
    </div>
  </div>

  <!-- EXPERIENCE TABLE -->
  <div class="dist-box">
    <div style="padding:14px 16px 10px;border-bottom:1px solid #e2e8f0;display:flex;align-items:center;gap:8px;">
      <span style="font-size:16px;">&#9203;</span>
      <span style="font-size:12px;font-weight:700;color:#475569;text-transform:uppercase;letter-spacing:1px;">Experience Bands</span>
    </div>
    <table style="width:100%;border-collapse:collapse;">
      <thead class="dist-thead">
        <tr>
          <th>Experience</th>
          <th>Distribution</th>
          <th>Headcount</th>
          <th>Share</th>
        </tr>
      </thead>
      <tbody class="dist-tbody">
        {exp_rows}
      </tbody>
    </table>
    <div class="dist-total">
      <span>Total Workforce</span>
      <strong>3,352</strong>
    </div>
  </div>

</div>

<!-- POD GRID -->
<div class="sec-hdr">&#128193; POD-Wise Updated Headcount</div>
<div class="pod-grid">{pod_cards}</div>

<!-- FOOTER NOTE -->
<div class="fnote">
  <strong>&#128204; Note:</strong> This dashboard tracks <b>onboardings only</b>.
  Headcount reflects cumulative active joiners per POD. Data refreshed daily at <b>11:00 AM IST</b>.
  Green &#9650; indicates new joiner today.
</div>

<!-- FOOTER -->
<div class="dash-footer">
  <div><strong style="color:#1e293b;">Joulestowatts Business Solutions Pvt. Ltd.</strong> &nbsp;&#183;&nbsp; <span class="tagline">Founder's Office</span></div>
  <div><span class="tagline">Time Matters</span> &nbsp;&#124;&nbsp; &#128231; talent@joulestowatts.com &nbsp;&#124;&nbsp; <span>Auto-generated &#183; Do not reply</span></div>
</div>

<script>
// Auto-resize iframe to exact content height — eliminates blank scroll
(function(){{
  function sendHeight(){{
    var h = document.body.scrollHeight;
    window.parent.postMessage({{type:"streamlit:setFrameHeight",height:h}},\"*\");
  }}
  window.addEventListener("load", sendHeight);
  window.addEventListener("resize", sendHeight);
  setTimeout(sendHeight,300);
  setTimeout(sendHeight,800);
}})();
</script>

<script>
// Auto-update refresh time display
function updateRefreshTime() {{
    var now = new Date();
    var hours = now.getHours();
    var minutes = now.getMinutes();
    var ampm = hours >= 12 ? 'PM' : 'AM';
    hours = hours % 12;
    hours = hours ? hours : 12;
    minutes = minutes < 10 ? '0'+minutes : minutes;
    var timeStr = hours + ':' + minutes + ' ' + ampm;
    var el = document.getElementById('refresh-time');
    if (el) {{ el.textContent = timeStr; }}
}}
updateRefreshTime();
</script>
</body></html>"""


GLOBAL_CSS = """
<style>
html,body,[data-testid="stAppViewContainer"],[data-testid="stMain"]{background:#f0f4f8!important;color:#1e293b;font-family:'Inter','Segoe UI',sans-serif;}
[data-testid="stSidebar"]{background:#f8fafc!important;border-right:1px solid #e2e8f0;transition:all 0.3s ease;}
[data-testid="stSidebar"] *{color:#374151!important;}
#MainMenu, footer { visibility: hidden; }
[data-testid="stDecoration"] { display: none; }
/* hide the header toolbar icons but NOT the sidebar toggle */
[data-testid="stHeader"] { background: transparent !important; }
[data-testid="stToolbar"] { visibility: hidden; }
[data-testid="stStatusWidget"] { visibility: hidden; }
iframe{border:none!important;}

/* ── collapsedControl must NEVER be hidden ── */
[data-testid="collapsedControl"],
[data-testid="collapsedControl"] *,
[data-testid="stSidebarCollapseButton"],
[data-testid="stSidebarCollapseButton"] * {
    visibility: visible !important;
    opacity: 1 !important;
    display: flex !important;
    pointer-events: auto !important;
}

/* ── Sidebar collapse toggle button styling ── */
[data-testid="stSidebarCollapseButton"] button,
[data-testid="collapsedControl"] button {
    background: #1f6feb !important;
    border: 2px solid #58a6ff !important;
    border-radius: 50% !important;
    width: 36px !important;
    height: 36px !important;
    color: #fff !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    box-shadow: 0 0 12px rgba(31,111,235,0.6) !important;
    padding: 0 !important;
    opacity: 1 !important;
    visibility: visible !important;
    pointer-events: auto !important;
    z-index: 99999 !important;
    position: fixed !important;
    cursor: pointer !important;
}
[data-testid="stSidebarCollapseButton"] button svg,
[data-testid="collapsedControl"] button svg {
    fill: #fff !important;
    color: #fff !important;
    width: 16px !important;
    height: 16px !important;
    visibility: visible !important;
    opacity: 1 !important;
    display: block !important;
}
/* position the re-open button when sidebar is collapsed */
[data-testid="collapsedControl"] {
    position: fixed !important;
    top: 48% !important;
    left: 4px !important;
    transform: translateY(-50%) !important;
    z-index: 999999 !important;
    opacity: 1 !important;
    visibility: visible !important;
    display: flex !important;
    pointer-events: auto !important;
    background: #1f6feb !important;
    border-radius: 0 8px 8px 0 !important;
    padding: 8px 4px !important;
    box-shadow: 4px 0 16px rgba(31,111,235,0.5) !important;
}

/* sidebar inner content spacing */
.s-sec{font-size:10px;color:#6e7681!important;text-transform:uppercase;letter-spacing:1px;font-weight:600;margin:12px 0 6px;}
.s-row{display:flex;justify-content:space-between;padding:6px 0;border-bottom:1px solid #e2e8f0;font-size:12px;}
.s-row:last-child{border-bottom:none;}
.s-lbl{color:#6e7681!important;}.s-val{font-weight:600;}
.s-val.g{color:#3fb950!important;}.s-val.b{color:#58a6ff!important;}
.s-mini{background:#e2e8f0;border-radius:8px;padding:10px 12px;margin-bottom:8px;}
.s-mini .lbl{font-size:10px;color:#64748b!important;text-transform:uppercase;letter-spacing:.8px;}
.s-mini .val{font-size:18px;font-weight:800;margin-top:2px;}
.s-mini.green .val{color:#15803d!important;}.s-mini.blue .val{color:#1d4ed8!important;}.s-mini.wh .val{color:#1e293b!important;}
@keyframes sb-pulse{0%,100%{box-shadow:0 0 0 0 rgba(63,185,80,.6);}50%{box-shadow:0 0 0 6px rgba(63,185,80,0);}}
.sb-live{display:inline-block;width:8px;height:8px;background:#3fb950;border-radius:50%;animation:sb-pulse 1.5s infinite;vertical-align:middle;margin-right:5px;}
</style>
"""

st.markdown(GLOBAL_CSS, unsafe_allow_html=True)

# Aggressive JS fix — watches DOM forever and ensures collapsed button stays visible & clickable
st.markdown("""
<script>
(function() {
    function fixCollapsedBtn() {
        // Fix the collapsed control container
        var collapsed = document.querySelector('[data-testid="collapsedControl"]');
        if (collapsed) {
            collapsed.style.setProperty('opacity',       '1',      'important');
            collapsed.style.setProperty('visibility',    'visible','important');
            collapsed.style.setProperty('display',       'flex',   'important');
            collapsed.style.setProperty('pointer-events','auto',   'important');
            collapsed.style.setProperty('z-index',       '999999', 'important');
            collapsed.style.setProperty('position',      'fixed',  'important');
            collapsed.style.setProperty('top',           '48%',    'important');
            collapsed.style.setProperty('left',          '4px',    'important');
            // Fix its button child
            var btn = collapsed.querySelector('button');
            if (btn) {
                btn.style.setProperty('opacity',       '1',    'important');
                btn.style.setProperty('visibility',    'visible','important');
                btn.style.setProperty('display',       'flex',  'important');
                btn.style.setProperty('pointer-events','auto',  'important');
                btn.style.setProperty('cursor',        'pointer','important');
            }
        }
        // Also fix the header itself - make sure it's not hidden
        var header = document.querySelector('header');
        if (header) {
            header.style.setProperty('visibility', 'visible', 'important');
        }
    }

    // Run immediately, then on interval, then watch DOM changes
    fixCollapsedBtn();
    setInterval(fixCollapsedBtn, 300);

    var observer = new MutationObserver(fixCollapsedBtn);
    document.addEventListener('DOMContentLoaded', function() {
        observer.observe(document.body, { childList: true, subtree: true, attributes: true, attributeFilter: ['style', 'class'] });
        fixCollapsedBtn();
    });
    // Also run on window load
    window.addEventListener('load', fixCollapsedBtn);
})();
</script>
""", unsafe_allow_html=True)

html_content = build_dashboard_html()
components.html(html_content, height=5650, scrolling=False)
