#!/usr/bin/env python3
"""
PDF to Markdown Converter
Converts PDF files to Markdown format using multiple methods
"""

import sys
import os
from pathlib import Path

def method1_pymupdf(pdf_path, output_path):
    """Method 1: Using PyMuPDF (fitz) - Best for text extraction"""
    try:
        import fitz  # PyMuPDF
        
        doc = fitz.open(pdf_path)
        markdown_content = []
        
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            text = page.get_text()
            
            # Add page header
            markdown_content.append(f"\n## Page {page_num + 1}\n")
            markdown_content.append(text)
            markdown_content.append("\n---\n")
        
        doc.close()
        
        # Write to file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.writelines(markdown_content)
        
        print(f"✅ Method 1 (PyMuPDF): Successfully converted to {output_path}")
        return True
        
    except ImportError:
        print("❌ PyMuPDF not installed. Install with: pip install PyMuPDF")
        return False
    except Exception as e:
        print(f"❌ Method 1 failed: {e}")
        return False

def method2_pdfplumber(pdf_path, output_path):
    """Method 2: Using pdfplumber - Good for tables and layout"""
    try:
        import pdfplumber
        
        markdown_content = []
        
        with pdfplumber.open(pdf_path) as pdf:
            for page_num, page in enumerate(pdf.pages):
                # Add page header
                markdown_content.append(f"\n## Page {page_num + 1}\n")
                
                # Extract text
                text = page.extract_text()
                if text:
                    markdown_content.append(text)
                
                # Extract tables
                tables = page.extract_tables()
                for table in tables:
                    markdown_content.append("\n### Table\n")
                    for row in table:
                        if row:
                            markdown_content.append("| " + " | ".join(str(cell) if cell else "" for cell in row) + " |\n")
                
                markdown_content.append("\n---\n")
        
        # Write to file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.writelines(markdown_content)
        
        print(f"✅ Method 2 (pdfplumber): Successfully converted to {output_path}")
        return True
        
    except ImportError:
        print("❌ pdfplumber not installed. Install with: pip install pdfplumber")
        return False
    except Exception as e:
        print(f"❌ Method 2 failed: {e}")
        return False

def method3_pypdf2(pdf_path, output_path):
    """Method 3: Using PyPDF2 - Simple text extraction"""
    try:
        import PyPDF2
        
        markdown_content = []
        
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            
            for page_num, page in enumerate(pdf_reader.pages):
                # Add page header
                markdown_content.append(f"\n## Page {page_num + 1}\n")
                
                # Extract text
                text = page.extract_text()
                markdown_content.append(text)
                markdown_content.append("\n---\n")
        
        # Write to file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.writelines(markdown_content)
        
        print(f"✅ Method 3 (PyPDF2): Successfully converted to {output_path}")
        return True
        
    except ImportError:
        print("❌ PyPDF2 not installed. Install with: pip install PyPDF2")
        return False
    except Exception as e:
        print(f"❌ Method 3 failed: {e}")
        return False

def method4_pdfminer(pdf_path, output_path):
    """Method 4: Using pdfminer.six - Advanced text extraction"""
    try:
        from pdfminer.high_level import extract_text
        
        # Extract all text at once
        text = extract_text(pdf_path)
        
        # Format as markdown
        markdown_content = [
            f"# PDF Content: {Path(pdf_path).name}\n\n",
            text
        ]
        
        # Write to file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.writelines(markdown_content)
        
        print(f"✅ Method 4 (pdfminer): Successfully converted to {output_path}")
        return True
        
    except ImportError:
        print("❌ pdfminer.six not installed. Install with: pip install pdfminer.six")
        return False
    except Exception as e:
        print(f"❌ Method 4 failed: {e}")
        return False

def install_dependencies():
    """Install required dependencies"""
    import subprocess
    
    packages = [
        "PyMuPDF",
        "pdfplumber", 
        "PyPDF2",
        "pdfminer.six"
    ]
    
    print("Installing PDF processing libraries...")
    for package in packages:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"✅ Installed {package}")
        except subprocess.CalledProcessError:
            print(f"❌ Failed to install {package}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python pdf_to_md_converter.py <pdf_file> [output_file]")
        print("       python pdf_to_md_converter.py --install-deps")
        return
    
    if sys.argv[1] == "--install-deps":
        install_dependencies()
        return
    
    pdf_path = sys.argv[1]
    
    if not os.path.exists(pdf_path):
        print(f"❌ File not found: {pdf_path}")
        return
    
    # Generate output filename
    if len(sys.argv) > 2:
        output_path = sys.argv[2]
    else:
        pdf_file = Path(pdf_path)
        output_path = pdf_file.with_suffix('.md')
    
    print(f"📄 Converting: {pdf_path}")
    print(f"📝 Output: {output_path}")
    print("-" * 50)
    
    # Try different methods in order of preference
    methods = [
        ("PyMuPDF (Recommended)", method1_pymupdf),
        ("pdfplumber (Good for tables)", method2_pdfplumber),
        ("pdfminer (Advanced)", method4_pdfminer),
        ("PyPDF2 (Simple)", method3_pypdf2),
    ]
    
    success = False
    for name, method in methods:
        print(f"🔄 Trying {name}...")
        if method(pdf_path, output_path):
            success = True
            break
    
    if not success:
        print("\n❌ All methods failed!")
        print("💡 Try installing dependencies with: python pdf_to_md_converter.py --install-deps")
    else:
        print(f"\n🎉 Conversion completed successfully!")
        print(f"📁 Output file: {output_path}")

if __name__ == "__main__":
    main()
