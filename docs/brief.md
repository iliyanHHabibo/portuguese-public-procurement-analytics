# Project brief: Public Procurement Spend Analytics (Portugal, 2022–2026)

7 November 2026 · Iliyan Habibo

## Scenario

A public-sector audit and advisory team wants visibility on Portuguese public procurement: where the money goes and how competitive the spending is. With the threshold reform in force since 1 October 2026, they also want a baseline of pre-reform patterns and an estimate of how many past contracts the new thresholds would affect.

*This is a self-defined scenario for a personal portfolio project; there is no real client.*

## Why now

Decreto-Lei 177/2026, in force since 1 October 2026, raised the maximum values for direct award and *consulta prévia*. For goods and services, direct award went from €20k to €75k and consulta prévia from €75k to €130k. For works, direct award went from €30k to €150k and consulta prévia from €150k to €1M.

Higher thresholds mean more contracts can now be awarded with less competition. A baseline of pre-reform patterns shows how many past contracts would have fallen into a less competitive procedure under the new limits, and gives a reference point for comparing post-reform data later.

## Business questions

1. **Where does the money go?** Which public bodies spend the most, on what (CPV), and how has that changed from 2022 to 2026?
2. **How competitive is it?** What share of contracts, by count and by value, goes through direct award, *consulta prévia* and public tender?
3. **How concentrated are suppliers?** Do a few companies win most of the contracts or most of the money, overall and within a buyer?
4. **Are there clusters just below the thresholds?** Contracts priced just under the old limits, between the same buyer and supplier: patterns worth reviewing, not proof of splitting.
5. **How often, and by how much, do contract prices change after signing?** Answered as far as the contracts data allows.
6. **What would the reform change?** How many past contracts would now qualify for a less competitive procedure?

## Scope

**In scope**

- Portal BASE contracts (*Contratos*), signed 2022 to September 2026: the only source for the core build.

**Out of scope**

- The *Anúncios* and *Modificações Contratuais* datasets. *Modificações* is a possible later extension for question 5.
- Other sources, such as INE population data for spend per person.
- Contracts from 1 October 2026 onwards, which fall under the new thresholds.
- Any legal judgement about specific public bodies or suppliers.

## Data source

Contratos Públicos – Portal BASE (IMPIC), published on [dados.gov.pt](https://dados.gov.pt/en/datasets/contratos-publicos-portal-base-impic-contratos-de-2012-a-2026/). Public domain, updated every two weeks, one JSON file per year. Snapshot downloaded on 13 October 2026: 1,035,687 contracts for 2022–2026, before the September 2026 cutoff is applied.

## Deliverables

1. **Pipeline:** a medallion lakehouse on Microsoft Fabric (bronze → silver → gold star schema), with data quality checks at every layer.
2. **Semantic model:** Direct Lake, with DAX measures for spend, competition, concentration and the reform.
3. **Report:** a Power BI report answering the six questions.
4. **Executive summary:** a short memo or slide deck with neutral findings, ending with what to investigate next.
5. **Documentation:** README, data dictionary and architecture diagram, in a public GitHub repo.

## Assumptions and limitations

- **Patterns, not proof.** Red flags such as direct awards or clusters below thresholds are patterns worth reviewing. Many are legal and justified.
- **Self-reported data.** Each public body enters its own contracts on Portal BASE, so quality varies: missing fields, input errors and inconsistent CPV codes. Data quality checks and their results are documented at each layer.
- **Question 5 is partial.** Without the *Modificações* dataset, it's limited to comparing contract price with effective price where both are filled in. When, why and how often contracts change is not covered.
- **2026 is partial and may be incomplete.** It covers January–September only, and contracts published after the 13 October 2026 snapshot are missing, so the latest months may be undercounted.
