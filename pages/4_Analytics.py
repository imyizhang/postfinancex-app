import postfinance
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

# Title
st.title("📊 Analytics")
st.caption("Powered by Tableau")

# Info
st.info(
    "This page provides a comprehensive report on the recorded customer calls"
)

# Tableau embed code
tableau_embed_code = (
    tableau_embed_code
) = """<div class='tableauPlaceholder' id='viz1716650958736' style='position: relative'><noscript>
                                          <a href='#'><img alt='Dashboard ' 
                                          src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;IB&#47;IBMDashboard_17165757578990&#47;Dashboard&#47;1_rss.png' 
                                          style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'>
                                          <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> 
                                          <param name='site_root' value='' /><param name='name' value='IBMDashboard_17165757578990&#47;Dashboard' />
                                          <param name='tabs' value='no' /><param name='toolbar' value='yes' />
                                          <param name='static_image' 
                                          value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;IB&#47;IBMDashboard_17165757578990&#47;Dashboard&#47;1.png' /> 
                                          <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' />
                                          <param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' />
                                          <param name='display_count' value='yes' /><param name='language' value='en-GB' /></object></div>                
                                          <script type='text/javascript'>                    
                                          var divElement = document.getElementById('viz1716650958736');                    
                                          var vizElement = divElement.getElementsByTagName('object')[0]; if ( divElement.offsetWidth > 800 ) 
                                          { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) 
                                          { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else 
                                          { vizElement.style.width='100%';vizElement.style.height='1627px';}   
                                          var scriptElement = document.createElement('script'); 
                                          scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js'; 
                                          vizElement.parentNode.insertBefore(scriptElement, vizElement); var hider = document.createElement('div'); 
                                          hider.style.height = "27px"; hider.style.width = "100%"; hider.style.position = "absolute"; 
                                          hider.style.backgroundColor = "white"; hider.style.zIndex = "2"; hider.style.bottom = "0"; 
                                          divElement.style.position = "relative"; divElement.appendChild(hider)  </script>"""


# Embed the iframe
components.html(tableau_embed_code, height=1000)
