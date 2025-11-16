function autoLinkContent(maxLinksPerPhrase = 3, maxTotalLinks = 10) {
    if (!window.AUTO_LINK_RULES || !Array.isArray(window.AUTO_LINK_RULES)) return;
  
    const container = document.querySelector("article#section-descriptions");
    if (!container) return;
  
    const walker = document.createTreeWalker(
      container,
      NodeFilter.SHOW_TEXT,
      {
        acceptNode: (node) => {
          const parent = node.parentNode;
          // Pomijamy jeśli w <a>, <script>, <style>, <noscript>, <img> itp.
          if (
            parent.closest("a") ||
            parent.closest("script, style, noscript, img")
          ) {
            return NodeFilter.FILTER_REJECT;
          }
          return NodeFilter.FILTER_ACCEPT;
        },
      },
      false
    );
  
    const usedCounts = {};
    let totalLinks = 0;
    const textNodes = [];
  
    // Zbieramy wszystkie akceptowalne tekstowe węzły
    while (walker.nextNode()) {
      textNodes.push(walker.currentNode);
    }
  
    // Iterujemy po nich i linkujemy frazy
    for (const node of textNodes) {
      if (totalLinks >= maxTotalLinks) break;
  
      let text = node.textContent;
      let replaced = false;
  
      for (const rule of window.AUTO_LINK_RULES) {
        const phrase = rule.phrase;
        const url = rule.url;
        const maxPerPhrase = maxLinksPerPhrase;
  
        if (
          (usedCounts[phrase] || 0) >= maxPerPhrase ||
          totalLinks >= maxTotalLinks
        ) {
          continue;
        }
  
        const regex = new RegExp(`\\b(${phrase})\\b`, "i");
        const match = text.match(regex);
        if (!match) continue;
  
        // Tworzymy nowy span z linkiem
        const span = document.createElement("span");
        const before = document.createTextNode(text.slice(0, match.index));
        const anchor = document.createElement("a");
        anchor.href = url;
        anchor.className = "auto-linked";
        anchor.textContent = match[0];
        const after = document.createTextNode(text.slice(match.index + match[0].length));
  
        span.appendChild(before);
        span.appendChild(anchor);
        span.appendChild(after);
  
        node.parentNode.replaceChild(span, node);
  
        usedCounts[phrase] = (usedCounts[phrase] || 0) + 1;
        totalLinks++;
        replaced = true;
        break; // Przerywamy, bo tekst node został zmieniony
      }
  
      if (replaced) {
        // cofamy się, żeby kontynuować w nowo dodanym `after`
        const newWalker = document.createTreeWalker(container, NodeFilter.SHOW_TEXT, null, false);
        textNodes.length = 0;
        while (newWalker.nextNode()) {
          const n = newWalker.currentNode;
          if (
            !n.parentNode.closest("a") &&
            !n.parentNode.closest("script, style, noscript, img")
          ) {
            textNodes.push(n);
          }
        }
      }
    }
  }
  