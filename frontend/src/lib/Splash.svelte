<script>
    import coverArt from "../assets/10.png";

    import { createEventDispatcher } from "svelte";

    const dispatch = createEventDispatcher();

    function changePage(page) {
        dispatch('page', page);
    }
</script>

<main>
    <div class="cover-box">
        <div class="image-box">
            <img src={coverArt} />
        </div>
        <div class="cover-text">
            <div class="title">Welcome to the Vector Embeddings Playground.</div>

            <p>
                Explore the mystical world of vector embeddings and language models.
                Here you can compare different
                models and metrics, play with KNN search, or even train your own
                embeddings using the tools provided here. The project is
                currently under development.
                You can find the full source code <a href="https://github.com/jeffhcs/embeddings-matrix">here</a>.
            </p>
            <div class="arrow-box">
                <p>Try it out!</p>
                <div class="arrow-down"></div>
            </div>

            <div class="links-box">
                <div class="demo-link" on:click={()=>changePage('matrix')}>Embeddings Comparison Matrix</div>
                <div class="demo-link" on:click={()=>changePage('search')}>Composite Embeddings Search</div>
                <div class="demo-link coming-soon">
                    Embeddings Visualizer (Coming Soon)
                </div>
            </div>
        </div>
    </div>
</main>

<style>
    a {
        color: var(--text);
        font-weight: bold;
    }
    main {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 95vh;
    }
    .cover-box {
        height: 70vh;
        width: min(150vh, 90vw);
        /* border: 2px solid black; */
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 2em;
    }
    .image-box {
        /* flex: 0, 0, 40%; */
        /* width: 40%; */
        /* padding: 2em;
        padding-right: 0; */
    }

    .cover-text {
        flex: 1;
    }

    .title {
        font-size: max(40px, 3vw);
        font-weight: bold;
    }

    img {
        height: 30vw;
    }

    p {
        font-size: max(20px, 1vw);
    }

    .demo-link {
        font-size: max(20px, 1vw);
        padding: 0.5em;
        border: 2px solid var(--text);
        border-radius: 5px;
        margin: 0.5em;
        cursor: pointer;

        transition:
            background-color 0.3s,
            color 0.3s;
    }
    .demo-link:hover {
        background-color: var(--text);
        color: var(--back);
    }

    .coming-soon:hover {
        background-color: #aa0000;
        color: white;
        cursor: not-allowed;
    }
    .arrow-box {
        text-align: center;
        margin-top: 3em;
        margin-bottom: 2em;
        line-height: 0;
        font-weight: bold;
    }

    .arrow-down {
        border: solid var(--text);
        border-width: 0 2px 2px 0;
        display: inline-block;
        padding: 3px;
        transform: rotate(45deg);
        -webkit-transform: rotate(45deg);
    }

    @media (max-width: 1200px) {
        .cover-box {
            flex-direction: column;
            margin-top: 10vh;
            margin-bottom: 10vh;
            height: 100%;
        }
        main {
            height: 100%;
        }
        img {
            height: min(80vw, 65vh);
        }
    }
</style>
