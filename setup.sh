mkdir -p ~/.streamlit/
printf "\n[server]\nport = %s\nenableCORS = false\nheadless = true\n" "$PORT" > ~/.streamlit/config.toml