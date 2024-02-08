<script>
    // import svelteLogo from './assets/svelte.svg'
    // import viteLogo from '/vite.svg'
    // import Counter from './lib/Counter.svelte'
    import Matrix from "./lib/Matrix.svelte";
    import Search from "./lib/Search.svelte";
    import Splash from "./lib/Splash.svelte";

    let currPage = "splash";

    function changePage(page) {
        console.log(page);
        currPage = page;
        window.scrollTo({
            top: 0,
            behavior: "smooth",
        });
    }

    let darkTheme = false;
    $: changeTheme(darkTheme);

    function changeTheme(darkTheme) {
        if (!darkTheme) {
            document.documentElement.style.setProperty("--text", "#000");
            document.documentElement.style.setProperty("--back", "#fff");
        } else {
            document.documentElement.style.setProperty("--text", "#fff");
            document.documentElement.style.setProperty("--back", "#000");
        }
    }
</script>

<main>
    <div class="sidebar-box">
        <div
            class="logo"
            on:click={() => {
                changePage("splash");
            }}
        >
            🥥 
            <!-- 🌴 -->
            <!-- 🏝️ -->
            Playground
        </div>
        <div class="sidebar">
            <div
                class="menu-item"
                on:click={() => {
                    changePage("matrix");
                }}
            >
                Embeddings Comparison Matrix
            </div>
            <div
                class="menu-item"
                on:click={() => {
                    changePage("search");
                }}
            >
                Composite Embeddings Search
            </div>
            <!-- <div class="menu-item">LLM Lesson Trees</div> -->
        </div>
    </div>
    <div class="theme-switch-wrapper">
        <label class="theme-switch" for="checkbox">
            <input type="checkbox" id="checkbox" bind:checked={darkTheme} />
            <div class="slider round">️</div>
        </label>
    </div>

    {#if currPage === "splash"}
        <Splash
            on:page={(e) => {
                changePage(e.detail);
            }}
        />
    {/if}
    {#if currPage === "search"}
        <Search />
    {/if}
    {#if currPage === "matrix"}
        <Matrix bind:darkTheme />
    {/if}
</main>

<style>
    /* .sidebar-box {
        position: absolute;
    } */
    main {
        font-family: "Courier New", Courier, monospace;
    }
    .container {
        position: relative;
        display: inline-block;
    }

    .sidebar {
        /* border: 1px solid #333; */
        position: fixed;
        top: 0;
        left: 0;
        width: 250px;
        /* background: none; */
        transform: translateX(-100%);
        transition:
            transform 0.3s ease,
            opacity 0.3s ease;
        opacity: 0;
        display: flex;
        flex-direction: column;
        align-items: flex-start; /* Align text to the left */
        padding-left: 2em; /* Padding to separate text from the edge */
        margin-top: 6em;
        background: rgba(var(--back), 0.9);
    }

    /* .sidebar-box {

        background: rgba(255, 255, 255, 0.8);
        position: fixed;
        top: 0;
        left: 0;
    } */

    .logo:hover + .sidebar,
    .sidebar:hover {
        transform: translateX(0);
        opacity: 1;
    }

    .logo {
        padding: 20px;
        cursor: pointer;
        z-index: 2;
        position: fixed;
        top: 0.5em;
        left: 0.5em;
        font-size: 1.5em;
        font-weight: bolder;
    }

    .logo:hover {
        text-decoration: underline;
    }

    .menu-item {
        padding: 0.5em 0;
        width: 100%;
        font-size: 1.2em;
        cursor: pointer;
    }

    .menu-item:hover {
        text-decoration: underline;
        font-weight: bold;
    }

    @media (max-width: 1200px) {
        .sidebar {
            position: absolute;
        }
        .logo {
            position: absolute;
        }
    }
    .theme-switch-wrapper {
        position: fixed;
        right: 20px;
        top: 25px;
        display: flex;
        align-items: center;
    }

    .theme-switch {
        display: inline-block;
        height: 34px;
        position: relative;
        width: 60px;
    }

    .theme-switch input {
        display: none;
    }

    .slider {
        background-color: var(--text);
        bottom: 0;
        cursor: pointer;
        left: 0;
        position: absolute;
        right: 0;
        top: 0;
        transition: 0.4s;
    }

    .slider:before {
        background-color: var(--back);
        bottom: 4px;
        content: "";
        height: 26px;
        left: 4px;
        position: absolute;
        transition: 0.4s;
        width: 26px;
    }

    /* input:checked + .slider {
    background-color: #66bb6a;
} */

    input:checked + .slider:before {
        transform: translateX(26px);
    }

    .slider.round {
        border-radius: 34px;
    }

    .slider.round:before {
        border-radius: 50%;
    }
</style>
