/**
 * CLOUDPOWER Palette — Tailwind CSS Extension
 * Cloud Power Inc. Official Color System
 * Version: 2.0.0
 *
 * 使い方:
 *   const cpColors = require('./tailwind.config.js');
 *   module.exports = {
 *     theme: {
 *       extend: { colors: cpColors.theme.extend.colors }
 *     }
 *   };
 */

module.exports = {
  theme: {
    extend: {
      colors: {
        // ---------- Primary (CP Blue) ----------
        primary: {
          50:  '#F2F8FC',
          100: '#D6E9F5',
          200: '#C5DDE9',
          300: '#A3CDE8',
          400: '#74B2E0',  // ★ Brand Color
          500: '#5A9BC7',
          600: '#4A8CC4',
          700: '#2E6BA6',
          800: '#245180',
          900: '#1A3A5C',
          DEFAULT: '#74B2E0'
        },

        // ---------- Gray Scale ----------
        gray: {
          50:  '#F8F8F8',
          100: '#F0F0F0',
          200: '#E0E0E0',
          300: '#CCCCCC',
          400: '#AAAAAA',
          500: '#888888',
          600: '#666666',
          700: '#4A4A4A',  // ★ Body
          800: '#333333',
          900: '#1A1A1A'
        },

        // ---------- Semantic ----------
        success: {
          50:  '#E6F5EB',
          300: '#7DD39B',
          500: '#28A745',
          700: '#1B7D3A',
          DEFAULT: '#28A745'
        },
        warning: {
          50:  '#FFF8E1',
          300: '#FFD666',
          500: '#F0AD00',
          700: '#C68A00',
          DEFAULT: '#F0AD00'
        },
        error: {
          50:  '#FDEAEA',
          300: '#F09DA5',
          500: '#DC3545',
          700: '#B71C1C',
          DEFAULT: '#DC3545'
        },
        info: {
          50:  '#F2F8FC',
          300: '#A3CDE8',
          500: '#74B2E0',
          700: '#2E6BA6',
          DEFAULT: '#74B2E0'
        },

        // ---------- Chart Accent (使用順) ----------
        chart: {
          1: '#74B2E0',  // CP Blue
          2: '#2E6BA6',  // Deep Blue
          3: '#5BBFB5',  // Teal
          4: '#F0AD00',  // Amber
          5: '#D4885C',  // Sand
          6: '#6B8FA3',  // Steel
          7: '#3D8B4A',  // Forest
          8: '#7A98AE'   // Slate
        },

        // ---------- Brand (ロゴ専用) ----------
        brand: {
          blue: '#74B2E0',
          gray: '#9E9E9F'  // ※ gray-500 (#888888) とは別物
        }
      },

      backgroundImage: {
        'cp-header-gradient': 'linear-gradient(135deg, #2E6BA6 0%, #74B2E0 100%)',
        'cp-header-gradient-dark': 'linear-gradient(135deg, #1A3A5C 0%, #2E6BA6 100%)'
      }
    }
  },

  darkMode: 'class'
};
