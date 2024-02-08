<script>
    import Cover from "./Cover.svelte";
    import SearchResults from "./SearchResults.svelte";

    let results = {
        unweighted: [
            {
                brand: "-",
                i: 1,
                image_url:
                    "https://product-images.metro.ca/images/hc2/h51/11860661469214.jpg",
                name: "Banana",
                unweighted_distance: 0.9995618973831403,
                unweighted_terms: "Banana",
                weighted_distance: 0.9994465386350329,
                weighted_terms: [["Banana", 1.0]],
            },
            {
                brand: "-",
                i: 2,
                image_url:
                    "https://product-images.metro.ca/images/hb2/hc2/8837350522910.jpg",
                name: "Coconut",
                unweighted_distance: 0.6428626080093451,
                unweighted_terms: "Coconut",
                weighted_distance: 0.6430760557665884,
                weighted_terms: [["Coconut", 1.0]],
            },
            {
                brand: "-",
                i: 3,
                image_url:
                    "https://assets.shop.loblaws.ca/products/20175355001/b2/en/front/20175355001_front_a06_@2.png",
                name: "Bananas, Bunch",
                unweighted_distance: 0.632573275376046,
                unweighted_terms: "Bananas, Bunch",
                weighted_distance: 0.8986254480284838,
                weighted_terms: [
                    ["Bananas", 1.0],
                    ["Bunch of Bananas", 0.5],
                ],
            },
            {
                brand: "-",
                i: 4,
                image_url:
                    "https://product-images.metro.ca/images/hd4/h39/8837093031966.jpg",
                name: "Cucumber",
                unweighted_distance: 0.5787691933543784,
                unweighted_terms: "Cucumber",
                weighted_distance: 0.577178739176152,
                weighted_terms: [["Cucumber", 1.0]],
            },
            {
                brand: "-",
                i: 5,
                image_url:
                    "https://product-images.metro.ca/images/he5/h03/8833632698398.jpg",
                name: "Plantain",
                unweighted_distance: 0.5596264985793779,
                unweighted_terms: "Plantain",
                weighted_distance: 0.5586800332628483,
                weighted_terms: [["Plantain", 1.0]],
            },
            {
                brand: "-",
                i: 6,
                image_url:
                    "https://product-images.metro.ca/images/hf0/h6f/9192030339102.jpg",
                name: "Carrot",
                unweighted_distance: 0.5576619120816377,
                unweighted_terms: "Carrot",
                weighted_distance: 0.5579861328456448,
                weighted_terms: [["Carrot", 1.0]],
            },
            {
                brand: "-",
                i: 7,
                image_url:
                    "https://product-images.metro.ca/images/h6d/h66/10723488858142.jpg",
                name: "Strawberries",
                unweighted_distance: 0.5545176118384382,
                unweighted_terms: "Strawberries",
                weighted_distance: 0.5539411151772593,
                weighted_terms: [["Strawberries", 1.0]],
            },
            {
                brand: "-",
                i: 8,
                image_url:
                    "https://assets.shop.loblaws.ca/products/20817066001/b2/en/front/20817066001_front_a06_@2.png",
                name: "Papaya",
                unweighted_distance: 0.5439590294622711,
                unweighted_terms: "Papaya",
                weighted_distance: 0.5437395263287799,
                weighted_terms: [["Papaya", 1.0]],
            },
            {
                brand: "-",
                i: 9,
                image_url:
                    "https://assets.shop.loblaws.ca/products/20116186001/b2/en/front/20116186001_front_a06_@2.png",
                name: "Carrots",
                unweighted_distance: 0.5398056787476537,
                unweighted_terms: "Carrots",
                weighted_distance: 0.5417269350993505,
                weighted_terms: [["Carrots", 1.0]],
            },
            {
                brand: "-",
                i: 10,
                image_url:
                    "https://product-images.metro.ca/images/ha8/he5/10406085951518.jpg",
                name: "Raspberries",
                unweighted_distance: 0.5330707259763687,
                unweighted_terms: "Raspberries",
                weighted_distance: 0.5331312043542362,
                weighted_terms: [["Raspberries", 1.0]],
            },
        ],
        weighted: [
            {
                brand: "-",
                i: 1,
                image_url:
                    "https://product-images.metro.ca/images/hc2/h51/11860661469214.jpg",
                name: "Banana",
                unweighted_distance: 0.9995618973831403,
                unweighted_terms: "Banana",
                weighted_distance: 0.9994465386350329,
                weighted_terms: [["Banana", 1.0]],
            },
            {
                brand: "Milk 2 Go",
                i: 2,
                image_url:
                    "https://assets.shop.loblaws.ca/products/20895935001/b2/en/front/20895935001_front_a06_@2.png",
                name: "Banana",
                unweighted_distance: 0.5722080186253182,
                unweighted_terms: "Milk 2 Go - Banana",
                weighted_distance: 0.9531315635756084,
                weighted_terms: [
                    ["Banana", 1.0],
                    ["Milk 2 Go Banana", 0.5],
                ],
            },
            {
                brand: "Dole",
                i: 3,
                image_url:
                    "https://product-images.metro.ca/images/hcd/h4d/8874222256158.jpg",
                name: "Organic Banana",
                unweighted_distance: 0.5164848271758062,
                unweighted_terms: "Dole - Organic Banana",
                weighted_distance: 0.9351388829926419,
                weighted_terms: [
                    ["Banana", 1.0],
                    ["Organic Banana", 0.5],
                    ["Dole Organic Banana", 0.2],
                ],
            },
            {
                brand: "-",
                i: 4,
                image_url:
                    "https://assets.shop.loblaws.ca/products/20175355001/b2/en/front/20175355001_front_a06_@2.png",
                name: "Bananas, Bunch",
                unweighted_distance: 0.632573275376046,
                unweighted_terms: "Bananas, Bunch",
                weighted_distance: 0.8986254480284838,
                weighted_terms: [
                    ["Bananas", 1.0],
                    ["Bunch of Bananas", 0.5],
                ],
            },
            {
                brand: "-",
                i: 5,
                image_url:
                    "https://assets.shop.loblaws.ca/products/20033488001/b2/en/front/20033488001_front_a06_@2.png",
                name: "Mini Bananas, Bunch",
                unweighted_distance: 0.49756371431326163,
                unweighted_terms: "Mini Bananas, Bunch",
                weighted_distance: 0.8706485850671271,
                weighted_terms: [
                    ["Bananas", 1.0],
                    ["Mini Bananas", 0.5],
                    ["Bunch of Mini Bananas", 0.2],
                ],
            },
            {
                brand: "-",
                i: 6,
                image_url:
                    "https://assets.shop.loblaws.ca/products/20047209001/b2/en/front/20047209001_front_a06_@2.png",
                name: "Red Bananas, Bunch",
                unweighted_distance: 0.49337575182572846,
                unweighted_terms: "Red Bananas, Bunch",
                weighted_distance: 0.8628824544997458,
                weighted_terms: [
                    ["Bananas", 1.0],
                    ["Red Bananas", 0.5],
                    ["Bunch of Red Bananas", 0.2],
                ],
            },
            {
                brand: "PC Organics",
                i: 7,
                image_url:
                    "https://assets.shop.loblaws.ca/products/20139509001/b2/en/front/20139509001_front_a06_@2.png",
                name: "Organic Bananas, Bunch",
                unweighted_distance: 0.4624275881985595,
                unweighted_terms: "PC Organics - Organic Bananas, Bunch",
                weighted_distance: 0.8562062238852037,
                weighted_terms: [
                    ["Bananas", 1.0],
                    ["Organic Bananas", 0.5],
                    ["Bunch of Organic Bananas", 0.2],
                    ["PC Organics Bananas", 0.1],
                ],
            },
            {
                brand: "-",
                i: 8,
                image_url:
                    "https://assets.shop.loblaws.ca/products/20649591001/b2/en/front/20649591001_front_a06_@2.png",
                name: "Manzano Bananas, Bunch",
                unweighted_distance: 0.4512794118064018,
                unweighted_terms: "Manzano Bananas, Bunch",
                weighted_distance: 0.8469642051813224,
                weighted_terms: [
                    ["Bananas", 1.0],
                    ["Manzano Bananas", 0.5],
                    ["Bunch of Manzano Bananas", 0.2],
                ],
            },
            {
                brand: "-",
                i: 9,
                image_url:
                    "https://assets.shop.loblaws.ca/products/21524604/b2/en/front/21524604_front_a06_@2.png",
                name: "Fresh Mango Pineapple Smoothie",
                unweighted_distance: 0.3606771094532421,
                unweighted_terms: "Fresh Mango Pineapple Smoothie",
                weighted_distance: 0.7057389400808318,
                weighted_terms: [
                    ["Mango", 1.0],
                    ["Pineapple", 1.0],
                    ["Smoothie", 0.5],
                    ["Mango Pineapple Smoothie", 0.2],
                    ["Fresh Mango Pineapple Smoothie", 0.1],
                ],
            },
            {
                brand: "-",
                i: 10,
                image_url:
                    "https://assets.shop.loblaws.ca/products/20022119/b2/en/front/20022119_front_a06_@2.png",
                name: "Tripak Fruit",
                unweighted_distance: 0.4069396224734667,
                unweighted_terms: "Tripak Fruit",
                weighted_distance: 0.6981268340967829,
                weighted_terms: [
                    ["Fruit", 1.0],
                    ["Tripak Fruit", 0.5],
                ],
            },
        ],
    };

    let weighted = true;
    let unweighted = false;

    let query_text = "banana";

    let search_bar;

    async function search() {
        const response = await fetch(
            `${window.location}/search?text=${query_text}`,
            // `http://localhost:5000/playground/search?text=${query_text}`,
        );
        const data = await response.json();
        results = data;
        search_bar.scrollIntoView({ behavior: "smooth" });
    }
</script>

<main>
    <Cover />

    <div class="search-bar" bind:this={search_bar}>
        <input placeholder="Enter query here..." bind:value={query_text} />
        <button on:click={search}>Search</button>
    </div>

    <div class="results">
        <SearchResults
            bind:results={results.unweighted}
            bind:weighted={unweighted}
        />
        <SearchResults bind:results={results.weighted} bind:weighted />
    </div>
</main>

<style>
    main {
        font-family: "Courier New", Courier, monospace;
        padding: 1em;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

    .search-bar {
        /* padding-left: 10%; */
        margin-bottom: 5em;
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 1em;
        width: min(80vw, 35em);
    }
    input {
        border: 2px solid var(--text);
        font-size: 1.5em;
        padding: 8px;
        width: 80%;
        font-family: "Courier New", Courier, monospace;
        background: var(--back);
        color: var(--text);
    }

    button {
        background-color: var(--text);
        color: var(--back);
        border: 3px solid var(--back);
        font-family: "Courier New", monospace;
        font-size: 1.5em;
        padding: 10px 20px;
        cursor: pointer;
        text-transform: uppercase;
        letter-spacing: 2px;
        transition:
            background-color 0.3s,
            color 0.3s;
    }

    button:hover {
        background-color: var(--back);
        color: var(--text);
        border-color: var(--text);
    }

    button:active {
        background-color: limegreen;
        color: var(--back);
        border-color: var(--back);
    }
    .results {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 2em;
    }
    @media (max-width: 900px) {
        .results {
            flex-direction: column;
        }
    }
</style>
