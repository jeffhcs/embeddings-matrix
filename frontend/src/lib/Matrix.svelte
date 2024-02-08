<script>
    import heatmap from "../assets/heatmap.png";
    let texts = `coffee shop
tea room
tea
earl grey
pineapple
coconut
`; // Bound to the textarea
    let model = "cohere"; // Default value for the model, bound to radio buttons
    let metric = "cosine"; // Default value for the metric, bound to radio buttons

    let loading = false;

    let imgSrc = heatmap;

    // Function to handle the form submission
    function handleSubmit() {
        const lines = texts.split("\n");

        const cleanedLines = lines
            .map((line) => line.trim())
            .filter((line) => line !== "");

        const cleanedText = cleanedLines.join("\n");
        const encodedTexts = encodeURIComponent(cleanedText);

        const url_base = window.location;

        const url = url_base + `/heatmap.png?texts=${encodedTexts}&model=${model}&metric=${metric}`;

        if (url !== imgSrc && cleanedText.length > 0) {
            imgSrc = url;
            loading = true;
        }
    }
    export let darkTheme;
</script>

<main>
    <div class="box">
        <div class="form">
            <div class="title">Embeddings Text</div>

            <textarea bind:value={texts} placeholder="Enter texts here..."
            ></textarea><br />

            <div>
                <label>Model:</label>
                <input type="radio" bind:group={model} value="cohere" />
                <label for="modelCohere">Cohere</label>
                <input type="radio" bind:group={model} value="openai" />
                <label for="modelOpenAI">OpenAI</label>
            </div>

            <div>
                <label>Metric:</label>
                <input type="radio" bind:group={metric} value="cosine" />
                <label for="metricCosine">Cosine</label>
                <input type="radio" bind:group={metric} value="dot" />
                <label for="metricDotProduct">Dot</label>

                <input type="radio" bind:group={metric} value="l2" />
                <label for="metricL2">L2</label>
            </div>

            <br />

            <button on:click|preventDefault={handleSubmit}>Submit</button>
        </div>
        <div>
            <div class="image-box">
                <div class="loading" class:hidden={!loading}>
                    <div class="lds-grid">
                        <div></div>
                        <div></div>
                        <div></div>
                        <div></div>
                        <div></div>
                        <div></div>
                        <div></div>
                        <div></div>
                        <div></div>
                    </div>
                </div>
                <img
                    id="resultImage"
                    src={imgSrc}
                    on:load={() => {
                        loading = false;
                    }}
                    class:invert-filter={darkTheme}
                />
            </div>
        </div>
    </div>
</main>

<style>
    main {
        font-size: 1.5rem;
        display: flex;
        justify-content: center;
    }

    .title {
        font-size: 1.2em;
        font-weight: bold;
        margin-bottom: 0.5em;
    }

    .form {
        padding-top: 30px;
    }

    .box {
        margin-top: 10vh;
        display: flex;
        /* flex-direction: row; */
        /* align-items: normal; */
        align-items: center;
        justify-content: space-between;
        gap: 2em;
        /* width: min(100vh, 100%); */
        /* max-width: 100%; */
        padding: 0 5vh;
        box-sizing: border-box;
    }
    .image-box {
        position: relative;

        width: min(90vh, min(10in, 50vw));
    }
    img {
        /* height: 100%; */
        /* max-width: 900px; */
        /* min-width: 50vw; */
        width: 100%;
        /* filter: invert(); */
    }
    .invert-filter {
        filter: invert(100%);
    }

    .hidden {
        display: none;
    }

    textarea {
        height: 50vh;
        font-size: 1.5rem;
        border: 3px solid var(--text);
        padding: 1em;
        width: min(30vw, 40vh);
        margin-bottom: 1em;
        background: var(--back);
        color: var(--text);
    }

    button {
        background-color: var(--text);
        color: var(--back);
        border: 3px solid var(--back);
        font-family: "Courier New", monospace;
        font-size: 16px;
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

    @media (max-width: 1200px) {
        .box {
            flex-direction: column;
            gap: 4em;
        }
        .image-box {
            width: min(10in, 80vw);
        }
        textarea {
            width: 70vw;
            height: 40vh;
        }
    }
    .loading {
        position: absolute;
        top: 9%;
        left: 7%;
        width: 75%;
        height: 80%;
        z-index: 2;
    }
    .lds-grid {
        display: inline-block;
        position: relative;
        width: 100%; /* Adjusted to fill the parent */
        height: 100%; /* Adjusted to fill the parent */
    }
    .lds-grid div {
        position: absolute;
        width: 20%; /* Adjusted relative size */
        height: 20%; /* Adjusted relative size */
        border-radius: 50%;
        background: #fff;
        animation: lds-grid 1.2s linear infinite;
    }

    /* Adjust positions to be relative */
    .lds-grid div:nth-child(1) {
        top: 10%;
        left: 10%;
        animation-delay: 0s;
    }
    .lds-grid div:nth-child(2) {
        top: 10%;
        left: 40%;
        animation-delay: -0.4s;
    }
    .lds-grid div:nth-child(3) {
        top: 10%;
        left: 70%;
        animation-delay: -0.8s;
    }
    .lds-grid div:nth-child(4) {
        top: 40%;
        left: 10%;
        animation-delay: -0.4s;
    }
    .lds-grid div:nth-child(5) {
        top: 40%;
        left: 40%;
        animation-delay: -0.8s;
    }
    .lds-grid div:nth-child(6) {
        top: 40%;
        left: 70%;
        animation-delay: -1.2s;
    }
    .lds-grid div:nth-child(7) {
        top: 70%;
        left: 10%;
        animation-delay: -0.8s;
    }
    .lds-grid div:nth-child(8) {
        top: 70%;
        left: 40%;
        animation-delay: -1.2s;
    }
    .lds-grid div:nth-child(9) {
        top: 70%;
        left: 70%;
        animation-delay: -1.6s;
    }

    @keyframes lds-grid {
        0%,
        100% {
            opacity: 1;
        }
        50% {
            opacity: 0.5;
        }
    }
</style>
