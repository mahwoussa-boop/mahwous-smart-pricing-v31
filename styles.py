"""
styles.py - v31.7 — بطاقات ذكية احترافية + عرض كل المنافسين بصورهم
"""
from html import escape as _html_escape
from textwrap import dedent
from datetime import datetime


def get_styles():
    return get_main_css()

def get_main_css():
    return """<style>
@import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700;900&display=swap');
*{font-family:'Tajawal',sans-serif!important}
.main .block-container{max-width:1400px;padding:1rem 2rem}

/* ── Stat Cards ── */
.stat-card{background:#111827;border-radius:12px;padding:16px;text-align:center;border:1px solid #1F293788;transition:all .3s ease}
.stat-card:hover{transform:translateY(-2px);box-shadow:0 8px 25px rgba(108,99,255,.2);border-color:#6C63FF}
.stat-card .num{font-size:2.2rem;font-weight:900;margin:4px 0}
.stat-card .lbl{font-size:.85rem;color:#8B8B8B}

/* ── بطاقة المنتج الذكية v31.7 ── */
.smart-card{background:#111827;border:1px solid #1F293788;border-radius:12px;margin:10px 0;overflow:hidden;transition:all .3s ease}
.smart-card:hover{border-color:#6C63FF55;box-shadow:0 4px 20px rgba(108,99,255,.12)}

.smart-card-header{display:flex;align-items:center;gap:14px;padding:14px 16px;border-bottom:1px solid #1F293744;direction:rtl}
.smart-card-img{width:64px;height:64px;border-radius:10px;object-fit:cover;border:2px solid #6C63FF;flex-shrink:0;background:#0e1628}
.smart-card-info{flex:1;min-width:0}
.smart-card-name{font-weight:700;color:#E2E8F0;font-size:.95rem;line-height:1.4;word-wrap:break-word}
.smart-card-meta{font-size:.72rem;color:#64748B;margin-top:3px;display:flex;gap:8px;flex-wrap:wrap;align-items:center}
.smart-card-meta span{display:inline-flex;align-items:center;gap:2px}
.smart-card-price-box{text-align:center;min-width:90px;flex-shrink:0;padding:6px 10px;background:rgba(108,99,255,.08);border-radius:8px}
.smart-card-our-price{font-size:1.3rem;font-weight:900;color:#818CF8}
.smart-card-our-label{font-size:.62rem;color:#64748B}

/* ── شريط المنافسين v31.7 ── */
.comp-list{padding:0 16px 12px;direction:rtl}
.comp-list-title{font-size:.72rem;color:#64748B;margin-bottom:6px;display:flex;align-items:center;gap:4px}
.comp-item{display:flex;align-items:center;gap:10px;padding:8px 10px;background:rgba(15,23,42,.6);border:1px solid #1F293766;border-radius:8px;margin:4px 0;transition:all .2s ease}
.comp-item:hover{border-color:#F59E0B44;background:rgba(245,158,11,.04)}
.comp-item.leader{border-color:#F59E0B55;background:rgba(245,158,11,.06)}
.comp-item-img{width:44px;height:44px;border-radius:8px;object-fit:cover;border:1px solid #333;flex-shrink:0;background:#0e1628}
.comp-item-info{flex:1;min-width:0}
.comp-item-store{font-weight:700;font-size:.78rem;color:#F59E0B;display:flex;align-items:center;gap:4px}
.comp-item-name{font-size:.72rem;color:#94A3B8;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;max-width:280px}
.comp-item-size{font-size:.62rem;color:#64748B}
.comp-item-price-box{text-align:center;min-width:80px;flex-shrink:0}
.comp-item-price{font-size:1rem;font-weight:900}
.comp-item-diff{font-size:.62rem;font-weight:600;margin-top:1px}

/* ── شريط الإجراءات والفرق ── */
.smart-card-footer{display:flex;justify-content:space-between;align-items:center;padding:8px 16px;background:rgba(15,23,42,.4);border-top:1px solid #1F293744;direction:rtl}
.diff-badge{padding:3px 10px;border-radius:8px;font-size:.78rem;font-weight:700;display:inline-flex;align-items:center;gap:4px}
.diff-red{background:rgba(239,68,68,.12);color:#EF4444;border:1px solid #EF444433}
.diff-green{background:rgba(16,185,129,.12);color:#10B981;border:1px solid #10B98133}
.diff-yellow{background:rgba(245,158,11,.12);color:#F59E0B;border:1px solid #F59E0B33}
.card-date{font-size:.58rem;color:#475569}

/* ── البطاقة المفقودة v31.7 ── */
.miss-card{border-radius:12px;padding:14px;margin:8px 0;background:linear-gradient(135deg,#0B0F19,#111827);border:1px solid #1F293788;transition:all .3s ease}
.miss-card:hover{border-color:#0EA5E944;box-shadow:0 4px 16px rgba(14,165,233,.08)}
.miss-card .miss-header{display:flex;justify-content:space-between;align-items:flex-start;gap:12px}
.miss-card .miss-info{flex:1;min-width:0}
.miss-card .miss-thumb{flex-shrink:0}
.miss-card .miss-name{font-weight:700;color:#38BDF8;font-size:1rem}
.miss-card .miss-meta{font-size:.75rem;color:#64748B;margin-top:4px}
.miss-card .miss-prices{text-align:left;min-width:120px}
.miss-card .miss-comp-price{font-size:1.2rem;font-weight:900;color:#F59E0B}
.miss-card .miss-suggested{font-size:.72rem;color:#10B981}

/* ── شارات ── */
.badge{display:inline-block;padding:2px 8px;border-radius:12px;font-size:.75rem;font-weight:700}
.b-high{background:rgba(239,68,68,.12);color:#EF4444;border:1px solid #EF444433}
.b-med{background:rgba(245,158,11,.12);color:#F59E0B;border:1px solid #F59E0B33}
.b-low{background:rgba(16,185,129,.12);color:#10B981;border:1px solid #10B98133}
.trust-badge{display:inline-block;padding:2px 8px;border-radius:10px;font-size:.68rem;font-weight:700;margin-left:4px}
.trust-green{background:rgba(16,185,129,.12);color:#10B981;border:1px solid #10B98133}
.trust-yellow{background:rgba(245,158,11,.12);color:#F59E0B;border:1px solid #F59E0B33}
.trust-red{background:rgba(239,68,68,.12);color:#EF4444;border:1px solid #EF444433}
.priority-badge{display:inline-flex;align-items:center;gap:3px;padding:2px 8px;border-radius:10px;font-size:.68rem;font-weight:700}
.priority-high{background:rgba(239,68,68,.12);color:#EF4444;border:1px solid #EF444433}
.priority-med{background:rgba(245,158,11,.12);color:#F59E0B;border:1px solid #F59E0B33}
.priority-low{background:rgba(16,185,129,.12);color:#10B981;border:1px solid #10B98133}

/* ── Table ── */
.cmp-table{width:100%;border-collapse:separate;border-spacing:0;border-radius:8px;overflow:hidden;font-size:.88rem}
.cmp-table thead th{background:#111827;color:#fff;padding:10px 8px;font-weight:700;text-align:center;border-bottom:2px solid #6C63FF;position:sticky;top:0;z-index:10}
.cmp-table tbody tr:nth-child(even){background:rgba(17,24,39,.4)}
.cmp-table tbody tr:hover{background:rgba(108,99,255,.06)!important}
.cmp-table td{padding:8px 6px;text-align:center;border-bottom:1px solid #1F293744;vertical-align:middle}
.td-our{background:rgba(108,99,255,.04)!important;border-right:3px solid #6C63FF;text-align:right!important;font-weight:600;color:#C4B5FD;max-width:250px;word-wrap:break-word}
.td-comp{background:rgba(245,158,11,.04)!important;border-left:3px solid #F59E0B;text-align:right!important;font-weight:600;color:#FCD34D;max-width:250px;word-wrap:break-word}

/* ── Buttons ── */
.action-btn{display:inline-block;padding:4px 10px;border-radius:6px;font-size:.75rem;font-weight:700;cursor:pointer;margin:2px;border:1px solid}
.btn-approve{background:rgba(16,185,129,.08);color:#10B981;border-color:#10B981}
.btn-remove{background:rgba(239,68,68,.08);color:#EF4444;border-color:#EF4444}
.btn-delay{background:rgba(245,158,11,.08);color:#F59E0B;border-color:#F59E0B}
.btn-export{background:rgba(108,99,255,.08);color:#818CF8;border-color:#818CF8}
.ai-box{background:#111827;padding:12px;border-radius:8px;border:1px solid #1F293788;margin:6px 0}
.paste-area{background:#0E1117;border:2px dashed #1F2937;border-radius:8px;padding:12px;min-height:80px}
.multi-comp{background:rgba(14,165,233,.04);border:1px solid rgba(14,165,233,.15);border-radius:6px;padding:8px;margin:4px 0}
.conf-bar{width:100%;height:6px;background:rgba(255,255,255,.06);border-radius:3px;overflow:hidden}
.conf-fill{height:100%;border-radius:3px}

/* ── Layout ── */
section[data-testid="stSidebar"]{background:linear-gradient(180deg,#0E1117,#111827);transition:all .3s ease}
#MainMenu,footer{visibility:hidden}
header[data-testid="stHeader"]{background:transparent!important;backdrop-filter:none!important}
[data-testid="stExpander"] summary svg,
[data-testid="stSelectbox"] svg[data-testid="stExpanderToggleIcon"],
details summary span[data-testid] svg{font-family:system-ui,-apple-system,sans-serif!important}
[data-testid="stExpander"] summary{direction:rtl;font-family:'Tajawal',sans-serif!important}
.stSelectbox label,.stMultiSelect label{direction:rtl;font-family:'Tajawal',sans-serif!important}
.st-key-page_num input{text-align:center!important;font-size:1.1rem!important;font-weight:700!important}
*{transition:color .15s ease,background .15s ease,border-color .15s ease}
button[data-testid]{transition:all .2s ease!important}
button[data-testid]:hover{transform:translateY(-1px)!important}

/* ── Sidebar Audit Button ── */
section[data-testid="stSidebar"] .st-key-nav_audit_tools button[data-testid="stBaseButton-secondary"],
section[data-testid="stSidebar"] .st-key-nav_audit_tools button[data-testid="stBaseButton-tertiary"]{
    background:transparent!important;border:1px solid rgba(51,51,68,.45)!important;border-radius:8px!important;
    color:rgba(250,250,250,.95)!important;font-weight:400!important;font-size:.9375rem!important;
    padding:.3rem .65rem!important;min-height:2.15rem!important;box-shadow:none!important;
    transition:background .15s ease,border-color .15s ease,color .15s ease!important}
section[data-testid="stSidebar"] .st-key-nav_audit_tools button:hover,
section[data-testid="stSidebar"] .st-key-nav_audit_tools button:focus-visible{
    background:rgba(108,99,255,.12)!important;border-color:rgba(108,99,255,.45)!important;color:#fff!important}
section[data-testid="stSidebar"] .st-key-nav_audit_tools button p{font-family:'Tajawal',sans-serif!important;font-size:.9375rem!important}

</style>"""


def get_sidebar_toggle_js():
    return """<style>
[data-testid="collapsedControl"]{color:#818CF8!important;background:linear-gradient(180deg,#818CF822,#6366F122)!important;border:1px solid #818CF844!important;border-radius:0 8px 8px 0!important;transition:all .25s ease!important}
[data-testid="collapsedControl"]:hover{background:linear-gradient(180deg,#818CF844,#6366F144)!important;box-shadow:3px 0 10px rgba(129,140,248,.4)!important}
</style>"""


def stat_card(icon, label, value, color="#818CF8"):
    return f'<div class="stat-card" style="border-top:3px solid {color}"><div style="font-size:1.3rem">{icon}</div><div class="num" style="color:{color}">{value}</div><div class="lbl">{label}</div></div>'


def _safe_float(v, default=0.0):
    try:
        return float(v)
    except (TypeError, ValueError):
        return default

def _safe_str(v, fallback=""):
    s = str(v or "").strip()
    return fallback if s.lower() in ("", "nan", "none", "<na>") else s

def _img_tag(url, w=64, h=64, border_color="#333", radius=10, css_class=""):
    u = _safe_str(url)
    if not u or not u.lower().startswith("http"):
        return ""
    eu = _html_escape(u, quote=True)
    cls = f'class="{css_class}"' if css_class else ""
    return (
        f'<img {cls} src="{eu}" '
        f'style="width:{w}px;height:{h}px;border-radius:{radius}px;object-fit:cover;'
        f'border:1px solid {border_color};background:#0e1628;flex-shrink:0" '
        f'loading="lazy" referrerpolicy="no-referrer" '
        f'onerror="this.style.display=\'none\'" />'
    )

def _linked_name(name, url="", color="#E2E8F0", max_len=120):
    safe = _html_escape(str(name or "")[:max_len])
    u = _safe_str(url)
    if u:
        eu = _html_escape(u, quote=True)
        return f'<a href="{eu}" target="_blank" style="color:{color};text-decoration:none" title="{_html_escape(str(name or ""), quote=True)}">{safe}</a>'
    return f'<span style="color:{color}">{safe}</span>'


def vs_card(our_name, our_price, comp_name, comp_price, diff, comp_source="",
            product_id="", our_img="", comp_img="", comp_url="", our_url="",
            accent_border="", row_bg="", compact=False,
            all_comps=None, brand="", size="", match_score=0, risk="",
            match_date=""):
    """
    بطاقة المنتج الذكية v31.7 — تعرض:
    - صورة + اسم منتجنا كاملاً مع الماركة والحجم
    - كل المنافسين بصورهم وأسعارهم مرتبين حسب السعر
    - فرق السعر + شارة الخطورة + تاريخ صغير
    """
    our_price = _safe_float(our_price)
    comp_price = _safe_float(comp_price)
    diff = _safe_float(diff)
    match_score = _safe_float(match_score)

    pid = _safe_str(product_id)
    pid_html = f'<span style="color:#64748B;font-size:.62rem">#{pid}</span>' if pid and pid != "0" else ""

    brand_s = _safe_str(brand, "")
    size_s = _safe_str(size, "")
    match_s = f'{match_score:.0f}%' if match_score > 0 else ""

    # Date
    date_s = _safe_str(match_date, datetime.now().strftime("%Y-%m-%d"))

    # ── Header: صورة منتجنا + اسمه الكامل + سعرنا ──
    our_img_html = _img_tag(our_img, 64, 64, "#818CF8", 10, "smart-card-img")
    our_name_html = _linked_name(our_name, our_url, "#E2E8F0", 200)

    meta_parts = []
    if brand_s: meta_parts.append(f'<span>🏷️ {_html_escape(brand_s)}</span>')
    if size_s: meta_parts.append(f'<span>📏 {_html_escape(size_s)}</span>')
    if match_s: meta_parts.append(f'<span>🎯 {match_s}</span>')
    if pid_html: meta_parts.append(pid_html)
    meta_html = " · ".join(meta_parts) if meta_parts else ""

    header = f'''<div class="smart-card-header">
{our_img_html}
<div class="smart-card-info">
<div class="smart-card-name">{our_name_html}</div>
<div class="smart-card-meta">{meta_html}</div>
</div>
<div class="smart-card-price-box">
<div class="smart-card-our-label">سعرنا</div>
<div class="smart-card-our-price">{our_price:,.0f}</div>
<div style="font-size:.58rem;color:#64748B">ر.س</div>
</div>
</div>'''

    # ── Competitors List: كل المنافسين بصورهم مرتبين بالسعر ──
    comp_rows = []

    # Build competitor list
    comps = []
    if all_comps:
        try:
            import pandas as pd
            if isinstance(all_comps, pd.DataFrame):
                comps = all_comps.to_dict("records") if not all_comps.empty else []
            elif isinstance(all_comps, list):
                comps = [dict(c) if isinstance(c, dict) else c for c in all_comps]
        except Exception:
            if isinstance(all_comps, list):
                comps = list(all_comps)

    if not comps and comp_name:
        comps = [{
            "competitor": comp_source or "منافس",
            "name": comp_name,
            "price": comp_price,
            "image_url": comp_img,
            "product_url": comp_url,
            "score": match_score,
            "size": size_s,
        }]

    # Sort by price
    comps = sorted(comps, key=lambda c: _safe_float(c.get("price", c.get("comp_price", 0))))

    if comps:
        for i, cm in enumerate(comps):
            c_store = _safe_str(cm.get("competitor", ""), "منافس")
            c_price_v = _safe_float(cm.get("price", cm.get("comp_price", 0)))
            c_name = _safe_str(cm.get("name", ""), "—")
            c_img_url = _safe_str(cm.get("image_url", cm.get("image", "")))
            c_url = _safe_str(cm.get("product_url", cm.get("url", "")))
            c_size = _safe_str(cm.get("size", ""), "")

            is_leader = (i == 0)
            leader_cls = "leader" if is_leader else ""
            crown = "👑 " if is_leader else ""
            price_color = "#F59E0B" if is_leader else "#94A3B8"

            # Diff from our price
            c_diff = our_price - c_price_v if (our_price > 0 and c_price_v > 0) else 0
            if c_diff > 0:
                diff_html = f'<div class="comp-item-diff" style="color:#EF4444">+{c_diff:,.0f}</div>'
            elif c_diff < 0:
                diff_html = f'<div class="comp-item-diff" style="color:#10B981">{c_diff:,.0f}</div>'
            else:
                diff_html = f'<div class="comp-item-diff" style="color:#F59E0B">= متساوي</div>'

            c_img_html = _img_tag(c_img_url, 44, 44, "#F59E0B33" if is_leader else "#333", 8, "comp-item-img")
            c_name_linked = _linked_name(c_name, c_url, "#94A3B8", 60)
            size_html = f'<div class="comp-item-size">📏 {_html_escape(c_size)}</div>' if c_size else ""

            comp_rows.append(f'''<div class="comp-item {leader_cls}">
{c_img_html}
<div class="comp-item-info">
<div class="comp-item-store">{crown}{_html_escape(c_store)}</div>
<div class="comp-item-name">{c_name_linked}</div>
{size_html}
</div>
<div class="comp-item-price-box">
<div class="comp-item-price" style="color:{price_color}">{c_price_v:,.0f} <span style="font-size:.6rem;color:#64748B">ر.س</span></div>
{diff_html}
</div>
</div>''')

    comp_count = len(comps)
    comp_section = ""
    if comp_rows:
        comp_section = f'''<div class="comp-list">
<div class="comp-list-title">👥 المنافسون ({comp_count}) — مرتبين بالسعر</div>
{''.join(comp_rows)}
</div>'''

    # ── Footer: فرق السعر + خطورة + تاريخ ──
    if diff > 0:
        diff_cls = "diff-red"
        diff_pct = f'+{(diff/comp_price*100):.0f}%' if comp_price > 0 else ""
        diff_text = f'↑ أعلى بـ {diff:,.0f} ر.س {diff_pct}'
    elif diff < 0:
        diff_cls = "diff-green"
        diff_pct = f'{(diff/comp_price*100):.0f}%' if comp_price > 0 else ""
        diff_text = f'↓ أقل بـ {abs(diff):,.0f} ر.س {diff_pct}'
    else:
        diff_cls = "diff-yellow"
        diff_text = '= سعر متساوي'

    risk_s = _safe_str(risk, "")
    risk_html = ""
    if "حرج" in risk_s:
        risk_html = '<span class="priority-badge priority-high">🔴 حرج</span>'
    elif "متوسط" in risk_s:
        risk_html = '<span class="priority-badge priority-med">🟡 متوسط</span>'
    elif "منخفض" in risk_s:
        risk_html = '<span class="priority-badge priority-low">🟢 منخفض</span>'

    footer = f'''<div class="smart-card-footer">
<div style="display:flex;align-items:center;gap:8px;flex-wrap:wrap">
<span class="diff-badge {diff_cls}">{diff_text}</span>
{risk_html}
</div>
<div class="card-date">📅 {_html_escape(date_s)}</div>
</div>'''

    return f'<div class="smart-card">{header}{comp_section}{footer}</div>'


def comp_strip(all_comps, our_price=None, rank_by_threat=False, show_threat_badge=False):
    """شريط المنافسين المصغر — يعرض كل المنافسين بأسعارهم واسم المنتج لديهم.

    - افتراضياً: ترتيب من **الأقل سعراً** (سلوك قديم).
    - إذا ``rank_by_threat=True`` و``our_price`` > 0: ترتيب بـ **Threat Score** (WTI) عند توفر ``utils.threat_score``.
    - يقبل ``list[dict]`` أو ``pandas.DataFrame`` (صفوف كمنافسين).
    """
    if all_comps is None:
        return ""
    try:
        import pandas as pd
        _has_pd = True
    except ImportError:
        pd = None
        _has_pd = False
    if _has_pd and isinstance(all_comps, pd.DataFrame):
        if all_comps.empty:
            return ""
        work = all_comps.to_dict("records")
    elif isinstance(all_comps, list):
        if len(all_comps) == 0:
            return ""
        work = [dict(c) if isinstance(c, dict) else c for c in all_comps]
    else:
        return ""
    if rank_by_threat and our_price is not None and float(our_price) > 0:
        try:
            from utils.threat_score import rank_competitors_for_ui
            sorted_comps = rank_competitors_for_ui(work, float(our_price))
        except Exception:
            sorted_comps = sorted(
                work, key=lambda c: float(c.get("price", c.get("comp_price", 0)) or 0)
            )
    else:
        sorted_comps = sorted(
            work, key=lambda c: float(c.get("price", c.get("comp_price", 0)) or 0)
        )
    rows = []
    for i, cm in enumerate(sorted_comps):
        c_store = str(cm.get("competitor", "")).strip()
        c_price = float(cm.get("price", cm.get("comp_price", 0)) or 0)
        c_pname = str(cm.get("name", "")).strip()
        c_score = float(cm.get("score", 0) or 0)
        c_img = str(cm.get("image_url", "") or cm.get("image", "") or "").strip()
        is_leader = (i == 0)
        crown = "👑" if is_leader else ""
        bg = "rgba(245,158,11,.06)" if is_leader else "rgba(108,99,255,.03)"
        border = "#F59E0B55" if is_leader else "#1F293766"
        name_color = "#F59E0B" if is_leader else "#94A3B8"
        short_pname = c_pname[:50] + ".." if len(c_pname) > 50 else c_pname
        score_html = f'<span style="color:#64748B;font-size:.62rem">{c_score:.0f}%</span>' if c_score > 0 else ""
        threat_html = ""
        if show_threat_badge and cm.get("threat_score") is not None:
            try:
                ts = float(cm["threat_score"])
                threat_html = (
                    f'<span style="color:#ff8a80;font-size:.58rem;margin-inline-start:4px" '
                    f'title="Threat Score">⚡{ts:.1f}</span>'
                )
            except (TypeError, ValueError):
                threat_html = ""
        img_html = _img_tag(c_img, 44, 44, border, 8)
        rows.append(
            f'<div style="display:flex;justify-content:space-between;align-items:center;'
            f'padding:6px 10px;background:{bg};border:1px solid {border};border-radius:8px;'
            f'margin:3px 0;gap:8px;flex-wrap:wrap">'
            f'<div style="display:flex;align-items:center;gap:6px;flex:1;min-width:0">'
            f'{img_html}'
            f'<span style="font-weight:900;font-size:.8rem">{crown}</span>'
            f'<span style="font-weight:700;color:{name_color};font-size:.75rem;white-space:nowrap">{c_store}</span>'
            f'<span style="color:#94A3B8;font-size:.7rem;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;max-width:300px" title="{c_pname}">{short_pname}</span>'
            f'{score_html}{threat_html}'
            f'</div>'
            f'<span style="font-weight:900;color:{"#F59E0B" if is_leader else "#94A3B8"};font-size:.85rem;white-space:nowrap">{c_price:,.0f} ر.س</span>'
            f'</div>'
        )
    return f'<div class="comp-strip" style="flex-direction:column;gap:2px;background:#0d1117;border:1px solid #1F293788;border-top:none;border-radius:0 0 8px 8px;padding:8px 12px;margin:0 0 2px 0">{chr(10).join(rows)}</div>'


def miss_card(name, price, brand, size, ptype, comp, suggested_price,
              note="", variant_html="", tester_badge="", border_color="#0EA5E933",
              confidence_level="green", confidence_score=0, image_url="",
              product_id="", comp_url="", title_override=""):
    """بطاقة المنتج المفقود v31.7"""
    safe_name = _html_escape(str(name or ""))
    safe_brand = _html_escape(str(brand or "—"))
    safe_size = _html_escape(str(size or "—"))
    safe_ptype = _html_escape(str(ptype or "—"))
    safe_comp = _html_escape(str(comp or "—"))
    safe_note = _html_escape(str(note or ""))
    trust_map = {
        "green":  ("trust-green",  "مؤكد"),
        "yellow": ("trust-yellow", "محتمل"),
        "red":    ("trust-red",    "مشكوك"),
    }
    t_cls, t_lbl = trust_map.get(confidence_level, ("trust-green", "مؤكد"))
    trust_html = f'<span class="trust-badge {t_cls}">{t_lbl}</span>' if confidence_level != "green" else ""

    note_html = f'<div style="font-size:.72rem;color:#F59E0B;margin-top:4px">{safe_note}</div>' if safe_note and "⚠️" in safe_note else ""

    img_html = _img_tag(image_url, 76, 76, "#1F293788", 10)
    if img_html:
        img_html = f'<div class="miss-thumb">{img_html}</div>'

    inner = f"""<div class="miss-card" style="border:1px solid {border_color}">
<div style="display:flex;gap:14px;align-items:flex-start;direction:rtl;flex-wrap:wrap">
{img_html}
<div style="flex:1;min-width:0">
<div class="miss-name">{trust_html}{tester_badge}{safe_name}</div>
<div class="miss-meta" style="margin-top:6px;line-height:1.5">🏷️ {safe_brand} &nbsp;|&nbsp; 📏 {safe_size} &nbsp;|&nbsp; 🧴 {safe_ptype} &nbsp;|&nbsp; 🏪 {safe_comp}</div>
{variant_html}
{note_html}
</div>
<div class="miss-prices" style="text-align:left;min-width:108px;flex-shrink:0">
<div class="miss-comp-price">{price:,.0f} ر.س</div>
<div class="miss-suggested" style="margin-top:4px">مقترح: {suggested_price:,.0f} ر.س</div>
</div>
</div>
</div>"""
    return dedent(inner).strip()


def lazy_img_tag(url, w=56, h=56, alt="", loading="lazy"):
    return _img_tag(url, w, h, "#333", 6)


def linked_product_title(name, url="", max_len=60):
    return _linked_name(name, url, "#38BDF8", max_len)
