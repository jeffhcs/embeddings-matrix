<main>
    <!-- <img src={coverArt} alt="cover art" /> -->
    <div class="cover">
        <div class="title">
            <span>Composite</span>
            <span>Vector</span>
            <span>Embeddings</span>
            <span>Search</span>
        </div>
        <div class="description">
            <p>
                One way to do embeddings for search is to simply
                concatenate the brand with the item name and embed this string
                directly. However, this string often becomes a jumble of terms
                that becomes difficult to untangle.
            </p>

            <p>
                Composite vector embeddings instead dissect items into
                weighted components which tend to yield more relevant search
                results.
                Each component term is embedded separately and then combined based on their weights.
            </p>
            <p>
                Displayed under each search result are the embedding texts (and
                weights for composite embeddings) with their dot product from the
                query text.
            </p>
        </div>
    </div>

    <div class="arrow-box">
        <p>Try it out!</p>
        <div class="arrow-down"></div>
    </div>
</main>

<style>
    .arrow-box {
        text-align: center;
        margin-bottom: 4em;
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
    main {

        width: 70vw;
    }

    .cover {
        display: flex;
        margin-top: 10vh;
        margin-bottom: 10vh;
        /* height: auto; */
    }
    .title-box {
        min-width: max(6em, 40%);
        min-height: 6em;
        /* background-color: #000; */
    }
    .title {
        font-weight: bolder;
        font-size: min(5vw, 5em);
        text-align: right;
        display: flex;
        flex-direction: column;
        padding-right: 1em;
        padding-top: 0.5em;
        box-sizing: border-box;


    }
    .description {
        /* flex: 1; */
        /* font-size: 1.3em; */
        font-size: max(1.2em, min(1.3vw, 1.5em));
        /* text-indent: 2em; */
    }

    @media (max-width: 1200px) {
        main {
            width: 75vw;
        }
        .cover {
            flex-direction: column;
        }
        .title {
            /* font-size: 4em; */
            font-size: max(4em, 7vw);
            text-align: center;
            display: inline;
        }

    }
    /* .cover {
            flex-direction: column;
        } */
</style>
