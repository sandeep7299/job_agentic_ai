@@
 from playwright.sync_api import sync_playwright
+import pandas as pd
 
@@
-        for link in soup.select("a.base-card__full-link"):
-            title = link.get_text(" ", strip=True)
-            print(f"{title}  →  {link['href'].split('?')[0]}")
+        rows = []
+
+        for card in soup.select("ul.jobs-search__results-list li"):
+            link    = card.select_one("a.base-card__full-link")
+            title   = link.get_text(" ", strip=True)
+            url     = link["href"].split("?")[0]
+            company = card.select_one("h4.base-search-card__subtitle").get_text(" ", strip=True)
+            location= card.select_one("span.job-search-card__location").get_text(" ", strip=True)
+
+            # open the posting in a background tab to grab description text
+            page2 = ctx.new_page()
+            page2.goto(url, timeout=0)
+            page2.wait_for_selector("div[data-test-description-section]", timeout=60000)
+            desc  = page2.query_selector("div[data-test-description-section]").inner_text()[:2000]
+            page2.close()
+
+            rows.append({
+                "title": title,
+                "company": company,
+                "location": location,
+                "url": url,
+                "description": desc
+            })
+
+        # --- save to Excel ----------------------------------------------
+        df = pd.DataFrame(rows)
+        fname = f"jobs_{pd.Timestamp.today().date()}.xlsx"
+        df.to_excel(fname, index=False)
+        print(f"\nSaved → {fname}  ({len(df)} rows)")

