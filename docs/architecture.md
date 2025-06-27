# Agentic Job-Application AI — Architecture Overview

> **Last updated:** 2025-06-26  
> Solo developer: Sandeep Mudhurakola

```mermaid
flowchart TD
    subgraph Phase0["Phase 0 · Prep"]
        A1(["Charter<br/>(<code>docs/charter.md</code>)"])
        A2(["CI pipeline<br/>(GitHub Actions)"])
    end

    subgraph Phase1["Phase 1 · Scraper MVP"]
        B1(["<code>linkedin_scrape.py</code><br/>Playwright"])
        B2["HTML → JSON<br/>(BeautifulSoup)"]
        B3["Save rows<br/>(Pandas → Excel)"]
        B4["Append rows<br/>(gspread → Google Sheets)"]
    end

    subgraph Phase2["Phase 2 · Tailoring & Autofill"]
        C1["LLM résumé tailor<br/>(OpenAI API)"]
        C2["Cover-letter gen"]
        C3["Playwright autofill<br/>(Easy Apply)"]
    end

    subgraph Phase3["Phase 3 · Semi-Autonomous"]
        D1["Multi-platform crawlers"]
        D2["Proxy / CAPTCHA"]
        D3["Email bot<br/>(IMAP + GPT)"]
        D4["Metrics dashboard"]
    end

    subgraph Phase4["Phase 4 · Full Agentic AI"]
        E1["RL feedback loop"]
        E2["Cloud scaling (AWS ECS)"]
        E3["Security & compliance"]
    end

    %% Links
    A1 --> A2
    A2 --> B1
    B1 --> B2 --> B3 --> B4 --> C1
    C1 --> C2 --> C3 --> D1
    D1 --> D2 --> D3 --> D4 --> E1
    E1 --> E2 --> E3
