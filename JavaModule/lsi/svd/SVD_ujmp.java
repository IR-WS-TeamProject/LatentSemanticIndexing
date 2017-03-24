package svd;

import java.math.BigDecimal;

import org.ujmp.core.Matrix;
import org.ujmp.core.SparseMatrix;

public class SVD_ujmp {

	public static void main(String[] args) {
		SparseMatrix m = SparseMatrix.Factory.zeros(2, 2);
		m.setAsDouble(1.0, 0, 0);
		m.setAsDouble(1.0, 1, 0);
		
		Matrix[] svd = m.svd();
		
		for (Matrix matrix : svd) {
			System.out.println(matrix.charValue() + ": " + matrix.getRowCount() + " x " + matrix.getColumnCount() + "; L1-Norm: " + matrix.getValueSum());
			
			for (BigDecimal[] row: matrix.toBigDecimalArray()){
				String row_string = "";
				for(BigDecimal e : row){
					row_string += e.toPlainString() + " ";
				}
				System.out.println(row_string);
			}
		}

	}

}
