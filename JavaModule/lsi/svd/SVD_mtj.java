package svd;

//https://en.wikipedia.org/wiki/Matrix_Toolkit_Java

import java.util.ArrayList;

import org.ojalgo.matrix.store.MatrixStore;

import no.uib.cipr.matrix.DenseMatrix;
import no.uib.cipr.matrix.Matrix;
import no.uib.cipr.matrix.Matrix.Norm;
import no.uib.cipr.matrix.MatrixEntry;
import no.uib.cipr.matrix.NotConvergedException;
import no.uib.cipr.matrix.SVD;
import no.uib.cipr.matrix.sparse.LinkedSparseMatrix;


public class SVD_mtj {

	public static void main(String[] args) throws NotConvergedException {
		Matrix m = new LinkedSparseMatrix(2, 2);
		m.add(0, 0, 1);
		m.add(1, 0, 1);
		
		//SVD svd = new SVD(m.numRows(),m.numColumns());
		SVD s = SVD.factorize(m);
		DenseMatrix U = s.getU();
		double[] S = s.getS();
		DenseMatrix Vt = s.getVt();
		
		System.out.println("U:" + U.numRows() + " x " + U.numColumns() + "; norm: " + U.norm(Norm.Frobenius));
		printMatrix(U);
		
		System.out.println("S (diagonal): length " + S.length);
		for (double e : S) {
			System.out.println(e);
		}
		
		System.out.println("Vt:" + Vt.numRows() + " x " + Vt.numColumns() + "; norm: " + Vt.norm(Norm.Frobenius));
		printMatrix(Vt);
	}
	public static void printMatrix(Matrix m){
		String[] rows = new String[m.numRows()];
		for (MatrixEntry matrixEntry : m) {
			if(rows[matrixEntry.row()] == null)
				rows[matrixEntry.row()] = String.valueOf(matrixEntry.get());
			else
				rows[matrixEntry.row()] = " " + String.valueOf(matrixEntry.get()); 
		}
		for (String string : rows) {
			System.out.println(string);
		}
	}
}
