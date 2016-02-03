<?xml version="1.0" encoding="utf-8" ?> 
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
	<xsl:output method="xml" version="1.0" encoding="UTF-8" indent="yes"/>
	<xsl:template match="/">

		<RECORD>			
		<xsl:for-each select="docs//doc//element">
		
			<xsl:element name="PROP">
				<xsl:attribute name="NAME">
					<xsl:value-of select="@name" />
				</xsl:attribute>		
				<xsl:element name="PVAL">
					<xsl:value-of select="./value" />
				</xsl:element>
			</xsl:element>
		        
		</xsl:for-each>
		</RECORD>

	</xsl:template>
</xsl:stylesheet>