# AI Deep Research Agent (CrewAI) 🚀

A powerful AI research agent built with CrewAI framework that performs comprehensive web research on any topic using multiple specialized agents working in collaboration. **Now with optimized research modes and fixed Firecrawl integration!**

## ✨ Latest Updates (v2.0)

- **⚡ Research Modes**: Fast (1-2 min), Standard (2-4 min), Deep (4-6 min)
- **🔧 Fixed Firecrawl Integration**: Proper deep research with FirecrawlApp
- **📊 Performance Optimization**: Reduced research time with smart defaults
- **🎯 Enhanced UI**: Progress indicators and estimated completion times
- **🛡️ Security**: Comprehensive API key validation and error handling

## 🚀 Features

- **Multi-Agent Architecture**: Uses CrewAI framework with specialized research and content writing agents
- **Deep Web Research**: Integrates with Firecrawl for comprehensive web crawling and analysis
- **Multiple AI Providers**: Support for OpenAI and Groq LLMs
- **Research Modes**: Choose between Fast, Standard, and Deep research modes
- **Real-time Progress Tracking**: Visual progress indicators during research
- **Export Options**: Download reports in Markdown, HTML, and JSON formats
- **Research History**: Save and review previous research sessions
- **Customizable Parameters**: Adjust research depth, time limits, and source limits
- **Debug Mode**: Detailed logging for troubleshooting

## 🏗️ Architecture

### Agents

1. **Research Analyst Agent**
   - Role: Conducts comprehensive web research using Firecrawl
   - Tools: Firecrawl deep research integration, web scraping fallback
   - Goal: Gather and analyze information from multiple sources
   - Output: Structured research findings with key insights

2. **Content Writer Agent**
   - Role: Creates comprehensive research reports
   - Input: Research findings from Research Analyst
   - Goal: Generate well-structured, professional reports
   - Output: Final research report with executive summary, key findings, and recommendations

### Research Modes

- **⚡ Fast Research (1-2 minutes)**
  - Depth: 1 (shallow)
  - Sources: 5
  - Time Limit: 1 minute
  - Perfect for quick overviews and initial research

- **📊 Standard Research (2-4 minutes)**
  - Depth: 2 (moderate)
  - Sources: 8
  - Time Limit: 2 minutes
  - Balanced speed and quality for most use cases

- **🔍 Deep Research (4-6 minutes)**
  - Depth: 3-5 (comprehensive)
  - Sources: 12-20
  - Time Limit: 4-10 minutes
  - For complex analysis and comprehensive reports

## 🛠️ Installation

### **📋 Prerequisites**

- **Python Version**: 3.11+ (required for latest dependencies)
  - Python 3.11+ includes sqlite3 >= 3.35.0 (required by ChromaDB)
  - Older versions may cause compatibility issues
  - Check your version: `python --version`

### **🚀 Quick Start**

1. **Clone the repository**
   ```bash
   git clone https://github.com/Elint-Agents/ai-deep-research-agent-crewai.git
   cd ai-deep-research-agent-crewai
   ```

2. **Create virtual environment (Python 3.11+ required)**
   ```bash
   python3.11 -m venv venv311
   source venv311/bin/activate  # On Windows: venv311\Scripts\activate
   ```

3. **Upgrade pip**
   ```bash
   pip install --upgrade pip
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Verify setup (optional but recommended)**
   ```bash
   python check_setup.py
   ```
   This will check Python version, dependencies, and API keys.

## 🔑 API Keys Setup

### Required API Keys

1. **OpenAI API Key** (or Groq API Key)
   - Get from: https://platform.openai.com/api-keys
   - Alternative: https://console.groq.com/keys

2. **Firecrawl API Key** (Optional but recommended)
   - Get from: https://firecrawl.dev
   - Enables deep web research capabilities
   - Without it, falls back to basic web scraping

### How to Use API Keys

1. **Run the application**: `streamlit run deep_research_crewai.py`
2. **Enter API keys** in the sidebar when the app loads
3. **Keys are stored securely** in Streamlit session state
4. **No .env file needed** - everything is handled through the UI

## 🚀 Usage

1. **Run the application**
   ```bash
   streamlit run deep_research_crewai.py
   ```

2. **Configure API Keys**
   - Enter your API keys in the sidebar
   - Choose your preferred AI provider (OpenAI or Groq)

3. **Select Research Mode**
   - **Fast Research**: Quick overviews (1-2 min)
   - **Standard Research**: Balanced approach (2-4 min)
   - **Deep Research**: Comprehensive analysis (4-6 min)

4. **Configure Research Parameters**
   - Research depth (1-5)
   - Time limit (1-10 minutes)
   - Max sources (5-20)

5. **Start Research**
   - Enter your research topic
   - Click "Start Research"
   - Monitor progress in real-time
   - Review and export results

## 📊 Research Process

1. **Initial Research Phase**
   - Research Analyst conducts deep web research using Firecrawl
   - Analyzes multiple sources and synthesizes information
   - Creates structured research findings

2. **Content Creation Phase**
   - Content Writer creates comprehensive research report
   - Includes executive summary, key findings, detailed analysis
   - Adds conclusions and recommendations

3. **Output Generation**
   - Final enhanced report with proper structure
   - Export options in multiple formats
   - Research metrics and history tracking

## 🎯 Use Cases

- **Academic Research**: Literature reviews, methodology analysis
- **Market Intelligence**: Competitive analysis, market trends
- **Technical Research**: Technology deep dives, implementation guides
- **News Analysis**: Current events, trend analysis
- **Business Intelligence**: Industry research, strategic planning
- **Quick Research**: Fast overviews for initial exploration

## 🔧 Configuration

### Research Parameters

- **Research Depth**: Controls how deep the search goes (1=shallow, 5=very deep)
- **Time Limit**: Maximum research time in minutes
- **Max Sources**: Maximum number of sources to analyze

### AI Provider Options

#### OpenAI
- **Models**: GPT-4, GPT-3.5-turbo
- **Speed**: Fast
- **Quality**: Excellent
- **Cost**: Pay-per-use

#### Groq
- **Models**: Llama 3.1, Mixtral, Gemma
- **Speed**: Very fast (optimized for speed)
- **Quality**: Good
- **Cost**: Often cheaper than OpenAI

## 📁 Project Structure

```
ai-deep-research-agent-crewai/
├── deep_research_crewai.py           # Main application file
├── requirements.txt                  # Python dependencies
├── README.md                        # This file
├── .gitignore                       # Git ignore rules
├── check_setup.py                   # Setup verification script
├── FIRECRAWL_FIX_SUMMARY.md         # Firecrawl integration details
└── RESEARCH_TIME_GUIDE.md           # Research time optimization guide
```

## 🔍 Key Improvements in v2.0

### **Fixed Firecrawl Integration**
- ✅ Proper `FirecrawlApp` usage instead of broken `firecrawl.Firecrawl`
- ✅ Correct `deep_research()` method with proper parameters
- ✅ Fallback to basic web scraping when Firecrawl unavailable

### **Research Mode Optimization**
- ⚡ **Fast Mode**: 1-2 minutes for quick overviews
- 📊 **Standard Mode**: 2-4 minutes for balanced research
- 🔍 **Deep Mode**: 4-6 minutes for comprehensive analysis

### **Performance Enhancements**
- 🚀 Smart default settings to reduce unnecessary processing
- 📊 Progress indicators with estimated completion times
- 🎯 Optimized agent workflows for faster results

### **Enhanced User Experience**
- 💡 Research tips and best practices
- 🔧 Debug mode for troubleshooting
- 📈 Research metrics and time tracking

## 🐛 Troubleshooting

### Common Issues

1. **Python Version Issues**
   - **Error**: `sqlite3` version too old
   - **Solution**: Upgrade to Python 3.11+ which includes sqlite3 >= 3.35.0
   - **Check**: Run `python check_setup.py` to verify your setup

2. **API Key Errors**
   - Ensure API keys are correctly entered
   - Check API key permissions and quotas
   - Verify provider selection matches API key

3. **Import Errors**
   - Ensure all dependencies are installed: `pip install -r requirements.txt`
   - Check Python version compatibility (3.11+ required)
   - Upgrade pip: `pip install --upgrade pip`
   - Run `python check_setup.py` to diagnose issues

4. **Firecrawl Errors**
   - Firecrawl API key is optional but recommended for best results
   - Check Firecrawl service status if using their API
   - App will fall back to basic web scraping if Firecrawl fails

5. **Research Time Issues**
   - Use **Fast Research Mode** for quicker results
   - Reduce research depth or max sources for large topics
   - Be specific in your research topic for better results

6. **Memory Issues**
   - Reduce research depth or max sources for large topics
   - Close other applications to free up memory
   - Use Fast Research Mode for memory-constrained environments

### Debug Mode

Enable debug mode in the sidebar to see:
- Detailed error messages
- API responses
- Agent thought processes
- Research tool outputs

## 💡 Research Tips

### **For Faster Results:**
- Use **Fast Research Mode** for quick overviews
- Be specific in your research topic
- Use shorter, focused queries

### **For Better Quality:**
- Use **Deep Research Mode** for comprehensive analysis
- Include context in your research topic
- Allow more time for complex subjects

### **For Optimal Performance:**
- Use Standard Research Mode for most use cases
- Balance between speed and depth based on your needs
- Monitor research metrics to optimize future searches

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **CrewAI Team**: For the excellent multi-agent framework
- **Firecrawl**: For advanced web research capabilities
- **OpenAI & Groq**: For powerful LLM APIs
- **Streamlit**: For the beautiful web interface # ai-deep-research-agent-crewai
