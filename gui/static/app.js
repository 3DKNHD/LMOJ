(() => {
  function norm(s) {
    const t = (s || "").toString().toLocaleLowerCase("es");
    try {
      return t.normalize("NFD").replace(/\p{M}/gu, "");
    } catch {
      return t;
    }
  }

  function tagList(row) {
    return (row.dataset.tags || "").split("|").map((t) => t.trim()).filter(Boolean);
  }

  function setQuery(values) {
    const url = new URL(window.location.href);
    Object.entries(values).forEach(([key, value]) => {
      if (!value || value === "all") url.searchParams.delete(key);
      else url.searchParams.set(key, value);
    });
    history.replaceState(null, "", url);
  }

  function setupProblems() {
    const form = document.getElementById("problem-filters");
    const table = document.getElementById("problem-table");
    if (!form || !table) return;

    const tbody = table.tBodies[0];
    const rows = Array.from(tbody.rows);
    const q = document.getElementById("q");
    const tag = document.getElementById("tag");
    const level = document.getElementById("level");
    const status = document.getElementById("status");
    const sort = document.getElementById("sort");
    const dir = document.getElementById("dir");
    const empty = document.getElementById("problem-empty");
    const count = document.getElementById("problem-count");
    const total = rows.length;
    const statusRank = { ac: 0, tried: 1, none: 2 };

    function updateSortButtons(key, direction) {
      table.querySelectorAll(".th-sort").forEach((btn) => {
        const active = btn.dataset.sort === key;
        btn.setAttribute("aria-sort", active ? (direction === "desc" ? "descending" : "ascending") : "none");
      });
    }

    function apply() {
      const query = norm(q.value.trim());
      const tagVal = tag.value;
      const levelVal = level.value;
      const statusVal = status.value;
      const sortKey = sort.value;
      const direction = dir.value === "desc" ? -1 : 1;

      const filtered = rows.filter((row) => {
        const hay = `${row.dataset.code} ${row.dataset.name} ${tagList(row).join(" ")}`;
        if (query && !norm(hay).includes(query)) return false;
        if (tagVal && !tagList(row).includes(tagVal)) return false;
        if (levelVal !== "all" && row.dataset.level !== levelVal) return false;
        if (statusVal !== "all" && row.dataset.status !== statusVal) return false;
        return true;
      });

      filtered.sort((a, b) => {
        let va = a.dataset[sortKey];
        let vb = b.dataset[sortKey];
        if (sortKey === "points" || sortKey === "tl") {
          va = Number(va);
          vb = Number(vb);
        } else if (sortKey === "status") {
          va = statusRank[va] ?? 9;
          vb = statusRank[vb] ?? 9;
        } else {
          va = norm(va);
          vb = norm(vb);
        }
        if (va < vb) return -1 * direction;
        if (va > vb) return 1 * direction;
        return norm(a.dataset.code).localeCompare(norm(b.dataset.code));
      });

      const shown = new Set(filtered);
      rows.forEach((row) => {
        row.style.display = shown.has(row) ? "" : "none";
      });
      filtered.forEach((row) => tbody.appendChild(row));

      const n = filtered.length;
      count.textContent = n === total ? `${total} problemas` : `${n} de ${total} problemas`;
      empty.hidden = n !== 0 || total === 0;
      table.hidden = n === 0;
      setQuery({
        q: q.value.trim(),
        tag: tagVal,
        level: levelVal,
        status: statusVal,
        sort: sortKey === "points" ? "" : sortKey,
        dir: dir.value === "asc" ? "" : dir.value,
      });
      updateSortButtons(sortKey, dir.value);
    }

    form.addEventListener("input", apply);
    form.addEventListener("change", apply);
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      apply();
    });
    document.getElementById("problem-reset").addEventListener("click", (e) => {
      e.preventDefault();
      q.value = "";
      tag.value = "";
      level.value = "all";
      status.value = "all";
      sort.value = "points";
      dir.value = "asc";
      apply();
      q.focus();
    });
    table.querySelectorAll(".th-sort").forEach((btn) => {
      btn.addEventListener("click", () => {
        if (sort.value === btn.dataset.sort) {
          dir.value = dir.value === "asc" ? "desc" : "asc";
        } else {
          sort.value = btn.dataset.sort;
          dir.value = "asc";
        }
        apply();
      });
    });
    table.addEventListener("click", (e) => {
      const chip = e.target.closest(".tag");
      if (!chip) return;
      tag.value = chip.dataset.tag;
      apply();
    });

    apply();
  }

  function setupHome() {
    const input = document.getElementById("home-filter");
    const table = document.getElementById("home-problem-table");
    if (!input || !table) return;
    const rows = Array.from(table.tBodies[0].rows);
    const empty = document.getElementById("home-empty");

    function apply() {
      const query = norm(input.value.trim());
      let n = 0;
      rows.forEach((row) => {
        if (!row.dataset.code) return;
        const hay = `${row.dataset.code} ${row.dataset.name} ${row.dataset.tags}`;
        const show = !query || norm(hay).includes(query);
        row.style.display = show ? "" : "none";
        if (show) n += 1;
      });
      empty.hidden = n !== 0;
    }

    input.addEventListener("input", apply);
  }

  function setupSubmissions() {
    const form = document.getElementById("sub-filters");
    const table = document.getElementById("sub-table");
    if (!form || !table) return;

    const rows = Array.from(table.tBodies[0].rows);
    const q = document.getElementById("sub-q");
    const problem = document.getElementById("sub-problem");
    const verdict = document.getElementById("sub-verdict");
    const lang = document.getElementById("sub-lang");
    const empty = document.getElementById("sub-empty");
    const count = document.getElementById("sub-count");
    const total = rows.length;

    function apply() {
      const query = norm(q.value.trim());
      const problemVal = problem.value;
      const verdictVal = verdict.value;
      const langVal = lang.value;
      let n = 0;
      rows.forEach((row) => {
        const hay = `${row.dataset.id} ${row.dataset.problem} ${row.dataset.verdict} ${row.dataset.lang}`;
        let show = true;
        if (query && !norm(hay).includes(query)) show = false;
        if (problemVal && row.dataset.problem !== problemVal) show = false;
        if (verdictVal !== "all" && row.dataset.verdict !== verdictVal) show = false;
        if (langVal !== "all" && row.dataset.lang !== langVal) show = false;
        row.style.display = show ? "" : "none";
        if (show) n += 1;
      });
      count.textContent = n === total ? `${total} envíos` : `${n} de ${total} envíos`;
      empty.hidden = n !== 0;
      table.hidden = n === 0;
      setQuery({
        q: q.value.trim(),
        problem: problemVal,
        verdict: verdictVal,
        lang: langVal,
      });
    }

    form.addEventListener("input", apply);
    form.addEventListener("change", apply);
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      apply();
    });
    document.getElementById("sub-reset").addEventListener("click", (e) => {
      e.preventDefault();
      q.value = "";
      problem.value = "";
      verdict.value = "all";
      lang.value = "all";
      apply();
      q.focus();
    });
    apply();
  }

  function setupSearchHotkey() {
    document.addEventListener("keydown", (e) => {
      if (e.key !== "/" || e.ctrlKey || e.metaKey || e.altKey) return;
      const tag = (e.target && e.target.tagName) || "";
      if (tag === "INPUT" || tag === "TEXTAREA" || tag === "SELECT" || e.target.isContentEditable) return;
      const box = document.getElementById("q") || document.getElementById("home-q") || document.getElementById("sub-q");
      if (!box) return;
      e.preventDefault();
      box.focus();
      box.select();
    });
  }

  setupProblems();
  setupHome();
  setupSubmissions();
  setupSearchHotkey();
})();
