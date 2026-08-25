import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------

st.set_page_config(
    page_title="E-Commerce Automation Testing",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------

st.markdown("""
<style>

.main {
    background-color: #f5f7fb;
}

.block-container {
    padding-top: 1rem;
    padding-left: 2rem;
    padding-right: 2rem;
}

.header {
    background: linear-gradient(90deg, #071a3d, #0d2d63);
    padding: 20px 25px;
    border-radius: 12px;
    color: white;
    margin-bottom: 20px;
}

.header h1 {
    margin: 0;
    font-size: 28px;
}

.header p {
    margin-top: 5px;
    color: #d8e5ff;
}

.card {
    background: white;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #e5e7eb;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    min-height: 130px;
}

.metric-title {
    color: #64748b;
    font-size: 14px;
}

.metric-value {
    font-size: 30px;
    font-weight: bold;
    margin-top: 8px;
}

.success {
    color: #16a34a;
}

.danger {
    color: #dc2626;
}

.warning {
    color: #d97706;
}

.info {
    color: #2563eb;
}

.section-title {
    font-size: 21px;
    font-weight: 700;
    margin-top: 25px;
    margin-bottom: 15px;
}

.feature {
    background: white;
    padding: 18px;
    border-radius: 10px;
    border: 1px solid #e5e7eb;
    margin-bottom: 10px;
}

.feature-title {
    font-weight: 600;
    font-size: 16px;
}

.feature-text {
    color: #64748b;
    font-size: 14px;
}

.sidebar-title {
    font-size: 20px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

with st.sidebar:

    st.markdown(
        '<div class="sidebar-title">🛒 E-Commerce Automation</div>',
        unsafe_allow_html=True
    )

    st.divider()

    menu = st.radio(
        "Navigation",
        [
            "🏠 Dashboard",
            "🧪 Test Execution",
            "🔌 API Testing",
            "🗄️ Database Testing",
            "📊 Reports",
            "🐞 Defects",
            "⚙️ Configuration"
        ]
    )

    st.divider()

    st.markdown("### Testing")

    st.write("🌐 Web Automation")
    st.write("🔥 Smoke Tests")
    st.write("🔄 Regression Tests")
    st.write("✅ Functional Tests")

    st.divider()

    st.markdown("### CI/CD")

    st.write("🔧 Jenkins Pipeline")
    st.write("🕐 Execution History")

    st.divider()

    st.markdown("""
    **Dharti Ghodke**

    QA Automation Engineer

    🟢 Online
    """)


# ---------------------------------------------------------
# DASHBOARD
# ---------------------------------------------------------

if menu == "🏠 Dashboard":

    st.markdown("""
    <div class="header">

    <h1>E-Commerce Automation Testing Framework</h1>

    <p>
    Web, API & Database Automation using Python, Selenium and PyTest
    </p>

    </div>
    """, unsafe_allow_html=True)

    # -----------------------------------------------------
    # PROJECT FEATURES
    # -----------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
        <div class="feature">

        <div class="feature-title">
        ✅ Selenium Web Automation
        </div>

        <div class="feature-text">
        Automated web application workflows using Selenium WebDriver.
        </div>

        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="feature">

        <div class="feature-title">
        🔌 API Automation
        </div>

        <div class="feature-text">
        REST API testing using Python Requests and Postman.
        </div>

        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="feature">

        <div class="feature-title">
        🗄️ Database Testing
        </div>

        <div class="feature-text">
        MySQL validation for application data.
        </div>

        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div class="feature">

        <div class="feature-title">
        🔥 Smoke, Regression & Functional
        </div>

        <div class="feature-text">
        Organized automated test suites using PyTest markers.
        </div>

        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="feature">

        <div class="feature-title">
        🔧 Jenkins CI/CD
        </div>

        <div class="feature-text">
        Automated test execution through Jenkins pipelines.
        </div>

        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="feature">

        <div class="feature-title">
        📊 Allure & HTML Reports
        </div>

        <div class="feature-text">
        Test execution reports for quality analysis.
        </div>

        </div>
        """, unsafe_allow_html=True)

    # -----------------------------------------------------
    # METRICS
    # -----------------------------------------------------

    st.markdown(
        '<div class="section-title">Test Summary</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="card">
        <div class="metric-title">TOTAL TESTS</div>
        <div class="metric-value info">128</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
        <div class="metric-title">PASSED</div>
        <div class="metric-value success">112</div>
        <div>87.5%</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
        <div class="metric-title">FAILED</div>
        <div class="metric-value danger">16</div>
        <div>12.5%</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="card">
        <div class="metric-title">SKIPPED</div>
        <div class="metric-value warning">0</div>
        <div>0%</div>
        </div>
        """, unsafe_allow_html=True)

    # -----------------------------------------------------
    # TEST RUN DATA
    # -----------------------------------------------------

    st.markdown(
        '<div class="section-title">Latest Test Runs</div>',
        unsafe_allow_html=True
    )

    test_runs = pd.DataFrame({
        "Build": ["#48", "#47", "#46", "#45", "#44"],
        "Environment": [
            "Chrome - Windows",
            "Chrome - Windows",
            "Firefox - Windows",
            "Chrome - Headless",
            "Chrome - Windows"
        ],
        "Status": [
            "Passed",
            "Passed",
            "Passed",
            "Failed",
            "Passed"
        ],
        "Tests": [42, 42, 38, 42, 42],
        "Passed": [38, 40, 33, 30, 41],
        "Failed": [4, 2, 5, 12, 1]
    })

    st.dataframe(
        test_runs,
        use_container_width=True,
        hide_index=True
    )

    # -----------------------------------------------------
    # CHART
    # -----------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            '<div class="section-title">Test Distribution</div>',
            unsafe_allow_html=True
        )

        chart_data = pd.DataFrame({
            "Status": ["Passed", "Failed"],
            "Count": [112, 16]
        })

        fig = px.pie(
            chart_data,
            names="Status",
            values="Count",
            hole=0.55
        )

        fig.update_layout(
            height=350,
            margin=dict(l=10, r=10, t=20, b=20)
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with col2:

        st.markdown(
            '<div class="section-title">Technologies Used</div>',
            unsafe_allow_html=True
        )

        technologies = [
            "🐍 Python",
            "🟢 Selenium",
            "🧪 PyTest",
            "🔌 REST API",
            "🗄️ MySQL",
            "🟠 Postman",
            "🔧 Jenkins",
            "🐙 GitHub",
            "📊 Allure",
            "🐳 Docker"
        ]

        for technology in technologies:
            st.write(f"• {technology}")

    # -----------------------------------------------------
    # DEFECTS
    # -----------------------------------------------------

    st.markdown(
        '<div class="section-title">Recent Defects</div>',
        unsafe_allow_html=True
    )

    defects = pd.DataFrame({
        "ID": ["BUG-048", "BUG-047", "BUG-046"],
        "Title": [
            "Login error message not displayed",
            "Add to cart not working",
            "Search with empty keyword"
        ],
        "Severity": [
            "High",
            "Medium",
            "Low"
        ],
        "Status": [
            "Open",
            "In Progress",
            "Closed"
        ]
    })

    st.dataframe(
        defects,
        use_container_width=True,
        hide_index=True
    )


# ---------------------------------------------------------
# TEST EXECUTION
# ---------------------------------------------------------

elif menu == "🧪 Test Execution":

    st.title("🧪 Test Execution")

    test_type = st.selectbox(
        "Select Test Suite",
        [
            "Smoke Tests",
            "Regression Tests",
            "Functional Tests",
            "All Tests"
        ]
    )

    browser = st.selectbox(
        "Browser",
        [
            "Chrome",
            "Firefox",
            "Edge"
        ]
    )

    environment = st.selectbox(
        "Environment",
        [
            "QA",
            "Staging",
            "Production"
        ]
    )

    if st.button("▶ Run Tests"):

        st.success(
            f"{test_type} started on {browser} / {environment}"
        )

        st.progress(100)

        st.write("Tests completed successfully.")


# ---------------------------------------------------------
# API TESTING
# ---------------------------------------------------------

elif menu == "🔌 API Testing":

    st.title("🔌 API Testing")

    endpoint = st.text_input(
        "API Endpoint",
        "https://jsonplaceholder.typicode.com/users"
    )

    method = st.selectbox(
        "HTTP Method",
        ["GET", "POST", "PUT", "DELETE"]
    )

    if st.button("Send Request"):

        import requests

        try:

            response = requests.request(
                method,
                endpoint,
                timeout=10
            )

            st.success(
                f"Status Code: {response.status_code}"
            )

            st.json(response.json())

        except Exception as error:

            st.error(str(error))


# ---------------------------------------------------------
# DATABASE TESTING
# ---------------------------------------------------------

elif menu == "🗄️ Database Testing":

    st.title("🗄️ Database Testing")

    st.info(
        "Database validation module for MySQL test environments."
    )

    query = st.text_area(
        "SQL Query",
        "SELECT COUNT(*) FROM users;"
    )

    if st.button("Execute Query"):

        st.warning(
            "Connect this dashboard to your test MySQL database "
            "before executing SQL queries."
        )

        st.code(query, language="sql")


# ---------------------------------------------------------
# REPORTS
# ---------------------------------------------------------

elif menu == "📊 Reports":

    st.title("📊 Test Reports")

    st.metric(
        "Automation Pass Rate",
        "87.5%"
    )

    st.metric(
        "Total Executions",
        "128"
    )

    st.metric(
        "Defects Found",
        "16"
    )

    st.info(
        "HTML and Allure reports can be generated from your PyTest test suite."
    )


# ---------------------------------------------------------
# DEFECTS
# ---------------------------------------------------------

elif menu == "🐞 Defects":

    st.title("🐞 Defect Management")

    defects = pd.DataFrame({
        "Bug ID": [
            "BUG-001",
            "BUG-002",
            "BUG-003"
        ],
        "Title": [
            "Login error message missing",
            "Cart validation failure",
            "Invalid search result"
        ],
        "Severity": [
            "High",
            "Medium",
            "Low"
        ],
        "Status": [
            "Open",
            "In Progress",
            "Closed"
        ]
    })

    st.dataframe(
        defects,
        use_container_width=True,
        hide_index=True
    )


# ---------------------------------------------------------
# CONFIGURATION
# ---------------------------------------------------------

elif menu == "⚙️ Configuration":

    st.title("⚙️ Configuration")

    st.text_input(
        "Application URL",
        "https://www.saucedemo.com/"
    )

    st.selectbox(
        "Default Browser",
        ["Chrome", "Firefox", "Edge"]
    )

    st.selectbox(
        "Execution Mode",
        ["Headed", "Headless"]
    )

    if st.button("Save Configuration"):

        st.success("Configuration saved successfully.")