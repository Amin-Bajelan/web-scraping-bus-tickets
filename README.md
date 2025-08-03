<!-- Full updated README with Selenium class usage -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
</head>
<body>

  <h1>🚌 Bus Ticket Web Scraper</h1>
  <p>This project is a Python-based web scraper designed to extract bus ticket information from travel websites using Selenium and save the data into structured CSV files for further analysis.</p>

  <h2>📌 Features</h2>
  <ul>
    <li>Automated scraping using <code>Selenium</code></li>
    <li>Headless browser navigation via <code>webdriver.Chrome()</code></li>
    <li>Data parsing and export using <code>pandas</code></li>
    <li>Class-based scraping logic for modular code</li>
  </ul>

  <h2>📁 Project Structure</h2>
  <table>
    <thead>
      <tr>
        <th>File</th>
        <th>Description</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><code>main.py</code></td>
        <td>Contains the <code>BusTicketScraper</code> class for scraping</td>
      </tr>
      <tr>
        <td><code>requirements.txt</code></td>
        <td>Python dependencies</td>
      </tr>
      <tr>
        <td><code>README.md</code></td>
        <td>Documentation for the project</td>
      </tr>
    </tbody>
  </table>

  <h2>🚀 Getting Started</h2>
  <ol>
    <li>Clone the repository:
      <pre><code>git clone https://github.com/Amin-Bajelan/web-scraping-bus-tickets.git
cd web-scraping-bus-tickets</code></pre>
    </li>
    <li>Install dependencies:
      <pre><code>pip install -r requirements.txt</code></pre>
    </li>
    <li>Run the script:
      <pre><code>python main.py</code></pre>
    </li>
  </ol>

  <h2>🧩 Key Technologies</h2>
  <ul>
    <li><code>Selenium</code>: Automates browser interactions</li>
    <li><code>webdriver.Chrome</code>: Launches headless Chrome browser</li>
    <li><code>pandas</code>: Stores and exports scraped data</li>
    <li><code>time</code>: Manages load delays</li>
  </ul>

  <h2>📦 Example Class Usage</h2>
  <pre><code>class BusTicketScraper:
    def __init__(self, url):
        self.url = url
        self.driver = self._init_driver()

    def _init_driver(self):
        options = Options()
        options.add_argument("--headless")
        return webdriver.Chrome(options=options)

    def scrape(self):
        self.driver.get(self.url)
        # extract data with find_element(s)
        self.driver.quit()</code></pre>

  <h2>💡 Future Improvements</h2>
  <ul>
    <li>Use WebDriverWait instead of time.sleep for smoother scraping</li>
    <li>Enable multi-site scraping support</li>
    <li>Add error handling and logging</li>
    <li>Optional GUI with <code>Streamlit</code></li>
  </ul>

  <h2>👤 Developer</h2>
  <p><a href="https://github.com/Amin-Bajelan" target="_blank">Amin Bajelan</a></p>

</body>
</html>
